from inp_parser import keyword_of_block
from section_ops import (
    remove_blocks,
    remove_blocks_by_keyword,
    remove_blocks_containing,
    remove_blocks_containing_in_keywords,
)

CONNECTOR_KEYWORDS = {
    "*CONNECTOR SECTION",
    "*CONNECTOR BEHAVIOR",
    "*CONNECTOR ELASTICITY",
    "*CONNECTOR DAMPING",
    "*CONNECTOR MOTION",
    "*CONNECTOR CONSTITUTIVE REFERENCE",
}

CONNECTOR_METADATA_KEYWORDS = {
    "*ELSET",
    "*NSET",
    "*SURFACE",
    "*ORIENTATION",
}

CONNECTOR_METADATA_PATTERNS = [
    "_CNS_",
    "CONN_",
    "DOOR-HINGE-LOW-LT-COUP",
    "DOOR-HINGE-UP-LT-COUP",
    "DOOR-LOCK-LT-COUP",
    "DOOR-LOCK-RT-COUP",
]

INACTIVE_BOUNDARY_PATTERNS = [
    "SET-521",
    "ERRORNODES",
]

FLUID_CAVITY_PATTERNS = [
    "BACK-LEFT-CAVITY",
    "BACK-RIGHT-CAVITY",
    "FRONT-LEFT-CAVITY",
    "FRONT-RIGHT-CAVITY",
    "FLUID PRESSURE",
]

def is_connector_element_block(block):
    first_line = block[0].strip().upper()
    return first_line.startswith("*ELEMENT") and "TYPE=CONN" in first_line

def is_removable_rigid_body_block(block):
    return keyword_of_block(block) == "*RIGID BODY" and not any(
        keep_name in line.upper() for line in block for keep_name in ("RIGID_POLE", "B_SET-519")
    )

def clean_model(blocks):
    removed = []

    # 1. remove constraint machinery
    blocks, r1 = remove_blocks_by_keyword(
        blocks,
        {
            "*TIE",
            "*COUPLING",
            "*DISTRIBUTING",
            "*MPC",
            "*EQUATION",
        },
    )
    removed.extend(r1)

    # 2. keep the crash pole and rigid road while removing the other rigid subsystems
    blocks, r2 = remove_blocks(
        blocks,
        is_removable_rigid_body_block,
        lambda block: f"Removed nonessential rigid body block: {block[0].strip()}",
    )
    removed.extend(r2)

    # 3. remove connector element/behavior definitions
    blocks, r3 = remove_blocks(
        blocks,
        is_connector_element_block,
        lambda block: f"Removed connector element block: {block[0].strip()}",
    )
    removed.extend(r3)

    blocks, r2 = remove_blocks_by_keyword(
        blocks,
        CONNECTOR_KEYWORDS,
    )
    removed.extend(r2)

    # 4. remove connector metadata blocks without deleting structural part definitions
    blocks, r4 = remove_blocks_containing_in_keywords(
        blocks,
        CONNECTOR_METADATA_PATTERNS,
        CONNECTOR_METADATA_KEYWORDS,
    )
    removed.extend(r4)

    # 5. remove any remaining connector-specific blocks that still reference connector names
    blocks, r5 = remove_blocks_containing(
        blocks,
        ["*CONNECTOR", "CONNECTOR"],
    )
    removed.extend(r5)

    # 6. remove boundary conditions tied to node sets that become inactive in the cleaned model
    blocks, r6 = remove_blocks_containing_in_keywords(
        blocks,
        INACTIVE_BOUNDARY_PATTERNS,
        {"*BOUNDARY"},
    )
    removed.extend(r6)

    # 7. remove automatic general contact for packaging diagnostics.
    # Abaqus 2024 is currently crashing in the package stage while building
    # contact domains, so this gives us a clean A/B test on the contact setup.
    blocks, r7 = remove_blocks_by_keyword(
        blocks,
        {
            "*CONTACT",
            "*CONTACT INCLUSIONS",
            "*SURFACE PROPERTY ASSIGNMENT",
        },
    )
    removed.extend(r7)

    # 8. remove tire cavity interactions and their dedicated cavity surfaces.
    # These are one of the last remaining interaction subsystems in the cleaned
    # deck and may still be sending Abaqus through contact auto-packaging.
    blocks, r8 = remove_blocks_by_keyword(
        blocks,
        {
            "*FLUID CAVITY",
            "*FLUID BEHAVIOR",
        },
    )
    removed.extend(r8)

    blocks, r9 = remove_blocks_containing_in_keywords(
        blocks,
        FLUID_CAVITY_PATTERNS,
        {
            "*SURFACE",
            "*SURFACE SECTION",
            "*INITIAL CONDITIONS",
        },
    )
    removed.extend(r9)

    return blocks, removed
