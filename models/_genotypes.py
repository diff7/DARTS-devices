Genotype(
    normal=[
        [("sep_conv_3x3", 1), ("sep_conv_3x3", 0)],
        [("skip_connect", 2), ("sep_conv_3x3", 0)],
        [("skip_connect", 2), ("sep_conv_3x3", 0)],
        [("sep_conv_3x3", 0), ("dil_conv_3x3", 1)],
    ],
    normal_concat=range(2, 6),
    reduce=[
        [("skip_connect", 0), ("max_pool_3x3", 1)],
        [("skip_connect", 2), ("sep_conv_3x3", 0)],
        [("skip_connect", 3), ("max_pool_3x3", 1)],
        [("skip_connect", 3), ("avg_pool_3x3", 1)],
    ],
    reduce_concat=range(2, 6),
)


Genotype(
    normal=[
        [("sep_conv_3x3", 1), ("sep_conv_3x3", 0)],
        [("skip_connect", 2), ("sep_conv_3x3", 0)],
        [("skip_connect", 2), ("sep_conv_3x3", 0)],
        [("sep_conv_3x3", 0), ("dil_conv_3x3", 1)],
    ],
    normal_concat=range(2, 6),
    reduce=[
        [("skip_connect", 0), ("max_pool_3x3", 1)],
        [("skip_connect", 2), ("sep_conv_3x3", 0)],
        [("max_pool_3x3", 1), ("skip_connect", 3)],
        [("skip_connect", 3), ("skip_connect", 2)],
    ],
    reduce_concat=range(2, 6),
)


######################


Genotype(
    normal=[
        [("dil_conv_3x3", 0), ("dil_conv_3x3", 1)],
        [("dil_conv_5x5", 2), ("sep_conv_3x3", 0)],
        [("sep_conv_5x5", 3), ("dil_conv_3x3", 1)],
        [("sep_conv_5x5", 3), ("sep_conv_5x5", 1)],
    ],
    normal_concat=range(2, 6),
    reduce=[
        [("max_pool_3x3", 0), ("max_pool_3x3", 1)],
        [("max_pool_3x3", 0), ("dil_conv_5x5", 2)],
        [("max_pool_3x3", 0), ("max_pool_3x3", 2)],
        [("max_pool_3x3", 0), ("sep_conv_5x5", 2)],
    ],
    reduce_concat=range(2, 6),
)