#!/usr/bin/env python3
import sys
import scanpy.api as sc
import matplotlib.pyplot as plt
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()
# sc.tl.pca(adata, n_comps=50, zero_center=True, svd_solver='auto', random_state=0, return_info=False, use_highly_variable=None, dtype='float32', copy=False, chunked=False, chunk_size=None)
# sc.pl.pca(adata)
# quit()
sc.pp.filter_genes(adata, min_counts = 1) #only consider genes with more than 1 count
sc.pp.normalize_per_cell(adata, key_n_counts = 'n_counts_all') #normalize with total UMI count per cell
filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor = 'cell_ranger', n_top_genes=1000, log = False)
adata = adata[:, filter_result.gene_subset] #filter genes
sc.pp.normalize_per_cell(adata)  # need to redo normalization after filtering
sc.pp.log1p(adata)
sc.pp.scale(adata)
sc.tl.pca(adata,n_comps=50)
sc.pp.neighbors(adata, n_neighbors=15, n_pcs=None, use_rep=None, knn=True, random_state=0, method='umap', metric='euclidean', metric_kwds={}, copy=False)
sc.tl.louvain(adata, resolution=None, random_state=0, restrict_to=None, key_added='louvain', adjacency=None, flavor='vtraag', directed=True, use_weights=False, partition_type=None, partition_kwargs=None, copy=False)
sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
sc.pl.tsne(adata, color=['louvain'])

