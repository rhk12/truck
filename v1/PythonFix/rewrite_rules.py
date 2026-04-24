from section_ops import remove_blocks_by_keyword, remove_blocks_containing

def clean_model(blocks):
    removed = []

    # 1. remove constraint machinery
    blocks, r1 = remove_blocks_by_keyword(
        blocks,
        {
            "*TIE",
            "*COUPLING",
            "*RIGID BODY",
            "*MPC",
            "*EQUATION",
        },
    )
    removed.extend(r1)

    # 2. remove ALL connector definitions
    blocks, r2 = remove_blocks_by_keyword(
        blocks,
        {
            "*CONNECTOR SECTION",
            "*CONNECTOR BEHAVIOR",
            "*CONNECTOR ELASTICITY",
            "*CONNECTOR DAMPING",
            "*CONNECTOR MOTION",
            "*CONNECTOR CONSTITUTIVE REFERENCE",
        },
    )
    removed.extend(r2)

    # 3. remove connector-related references
    blocks, r3 = remove_blocks_containing(
        blocks,
        [
            "CONN_",
            "CONNECTOR",
            "DOOR-HINGE",
            "DOOR-LOCK",
        ],
    )
    removed.extend(r3)

    return blocks, removed
