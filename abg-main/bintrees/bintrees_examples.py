# -*- coding: utf-8 -*-
"""
BinTree: examples used in exercises
"""

from algo_py import bintree
from algo_py.bintree import BinTree# to allow to use BinTree instead of bintree.BinTree


# --- FIGURE 1 (Reprise en Figure 9 / Figure 12) ---
tree_fig1 = BinTree(5,
    BinTree(2,
        BinTree(-1,
            BinTree(4, None, None),
            None
        ),
        BinTree(0,
            None,
            BinTree(11, None, None)
        )
    ),
    BinTree(12,
        BinTree(4, None, None),
        BinTree(1,
            BinTree(-2,
                None,
                BinTree(15, None, None)
            ),
            None
        )
    )
)

# --- FIGURE 2 ---
tree_fig2 = BinTree('V',
    BinTree('D',
        BinTree('I',
            BinTree('Q',
                None,
                BinTree('U', None, None)
            ),
            None
        ),
        BinTree('S',
            BinTree('E', None, None),
            BinTree('T', None, None)
        )
    ),
    BinTree('I',
        BinTree('E',
            None,
            BinTree('R', None, None)
        ),
        BinTree('A',
            BinTree('T', None, None),
            BinTree('S', None, None)
        )
    )
)

# --- FIGURE 3 (B2) ---
tree_b2 = BinTree(1,
    BinTree(2,
        BinTree(4,
            BinTree(8, None, None),
            BinTree(9, None, None)
        ),
        BinTree(5, None, None)
    ),
    BinTree(3, None, None)
)

# --- FIGURE 4 (B3) ---
tree_b3 = BinTree(15,
    BinTree(8,
        BinTree(1, None, None),
        BinTree(12,
            None,
            BinTree(10, None, None)
        )
    ),
    BinTree(28,
        BinTree(20,
            None,
            BinTree(23, None, None)
        ),
        BinTree(42,
            BinTree(35, None, None),
            BinTree(66, None, None)
        )
    )
)

# --- FIGURE 5 (Identique à la FIGURE 7 - Arbre B) ---
tree_b = BinTree(0,
    BinTree(1,
        BinTree(2, None, None),
        BinTree(3,
            None,
            BinTree(4, None, None)
        )
    ),
    BinTree(5,
        BinTree(6,
            None,
            BinTree(7, None, None)
        ),
        BinTree(8,
            None,
            BinTree(9, None, None)
        )
    )
)

# --- FIGURE 8 (transpose(B)) ---
tree_transpose_b = BinTree(0,
    BinTree(10,
        BinTree(16,
            BinTree(18, None, None),
            None
        ),
        BinTree(12,
            BinTree(14, None, None),
            None
        )
    ),
    BinTree(2,
        BinTree(6,
            BinTree(8, None, None),
            None
        ),
        BinTree(4, None, None)
    )
)

# --- FIGURES 10, 11, 12 (Exercice 7.2 Somme) ---
tree_sum_b1 = BinTree(8,
    BinTree(6, None, None),
    BinTree(2, None, None)
)

tree_sum_b2 = BinTree(8,
    BinTree(6,
        BinTree(5, None, None),
        BinTree(1, None, None)
    ),
    BinTree(2,
        BinTree(1, None, None),
        BinTree(1, None, None)
    )
)

tree_sum_b3 = BinTree(8,
    BinTree(6,
        BinTree(5, None, None),
        BinTree(3, None, None)
    ),
    BinTree(2,
        BinTree(1, None, None),
        BinTree(1, None, None)
    )
)
