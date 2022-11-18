//Dataset input
//
//Set Up-
//  read in data file
//  store each data from dataset- in a list of pointers to nodes
//
//procedure 1: 
//  Input(list data structure containing data values)
//  Output(DTW Distance values, in matrix representation)
//
//  Description- (calculate pairwise distance between every pair time series using DTW distance)
//
//procedure 2: 
//  Input(DTW matrix containing distance values)
//  Output(Adjacentcy list)
//
//  Description- (for a threashold k, generate adjacency list,
//                if data-i,j > k, set A-i,j to 0; otherwise set A-i,j to 1)
//                edges exist between the nodes if the DTW distance between nodes is less than k
//
//
//Data output finished datafile as-
//            node, edge list
//            representation
//
//
//Compairing threashold values:(for improved clustering)
//  Homogeneity scores are computed using diffrent thresholds k
//  k leading to the highest homogeneity score is chosen as the final
//  parameter, (range from minD(i, j) to maxD(i, j)