# COMPASS: Cardinal Orientation Manipulation and Pattern-Aware Spatial Search

This git repository is for the work **COMPASS: Cardinal Orientation Manipulation and Pattern-Aware Spatial Search** presented at the 2nd ACM SIGSPATIAL International Workshop on Searching and Mining Large Collections of Geospatial Data in November 2023, [available online](https://dl.acm.org/doi/pdf/10.1145/3615890.3628537). 

## Presentation

The workshop presentation is available in the [presentations directory](https://github.com/osullik/COMPASS_GEOSEARCH/tree/main/presentations), along with a recording of the talk. 

## Research Abstract: 

The Spatial Pattern Matching paradigm offers a promising direction for searching with incomplete or imperfect information, but it is badly constrained by dependence on graph-based representations and computationally intensive search algorithms like subgraph matching and constraint satisfaction. To address these limitations, we present COMPASS, a suite of data structures and algorithms that enable pattern-based search by encoding the directional relationships between objects in abstracted matrix representations rather than graph structures. We provide a series of recursive search algorithms that leverage our matrix representations to enable spatial search queries with directional constraints, which are typically too dense for previous graph-based approaches. Our search methods find matches even when the query pattern is not aligned to the global coordinate system, resulting in perfect recall in our evaluation. Computationally, our search methods scale with the number of query objects times the number of database objects squared in the worst case, which is significantly better than previous methods. Our empirical measurements show that the performance is typically even better, approaching logarithmic in the number of query terms.

## Replicating the Experiments:

Our code is maintained in the [GESTALT Repo](https://github.com/osullik/GESTALT)

Start by cloning the repo and following the instructions on the repo readme for building the virtual environment:

    git clone https://github.com/osullik/GESTALT.git

[Optional] Regenerate the experiment data. 

*All experiment data and results from our runs are available on this repo in the [data directory](https://github.com/osullik/COMPASS_GEOSEARCH/tree/main/data)*

change to the appropriate directory (assuming your start point is ~/GESTALT)

    cd code/experiments

run the experiment scripts: 

    sh geosearch_experiment_runner.sh

    sh geosearch_experiment_runner_pow2.sh

    sh geosearch_experiment_runner_pow2_locs.sh

Explore the results with our [jupyter notebook](https://github.com/osullik/GESTALT/blob/main/code/COMPASS_experimental_analysis.ipynb)


## Building the Videos

Visual descriptions of our algorithms are available as videos created with the Manim package.

[Location Object Search](https://github.com/osullik/COMPASS_GEOSEARCH/blob/main/presentations/01_LocationObjectSearch.mp4)

[Object Object Search](https://github.com/osullik/COMPASS_GEOSEARCH/blob/main/presentations/02_ObjectObjectSearch.mp4)

[Cardinality Invariant Methods](https://github.com/osullik/COMPASS_GEOSEARCH/blob/main/presentations/03_CardinalityInvariant.mp4)

To recompile from source, navigate to the directory: 

    cd presentations/code

Install Manim:

  [Manim Installation Guide](https://docs.manim.community/en/stable/installation.html#local-installation)

Create a virtual environment: 

    python -m venv anim_env 

Activate the environment: 

    source anim_env/bin/activate

Install dependencies

    pip install -r requirements.txtx  x

Compile the videos

    manim -pql loc-obj.py LocationObjectSearch

    mainm -pql obj-obj.py ObjectObjectSearch

    mainm -pql cardinality_invariant.py CardinalityInvariant

## Citing the work

If you use this work, please cite it as: 

  @inproceedings{Osullivan2023,
  title={COMPASS: Cardinal Orientation Manipulation and Pattern-Aware Spatial Search},
  author={O'Sullivan, Kent and Schneider, Nicole R and Samet, Hanan},
  booktitle={Proceedings of the 2nd ACM SIGSPATIAL International Workshop on Searching and Mining Large Collections of Geospatial Data},
  pages={1--8},
  year={2023}
}

## Contact

If you have any questions please reach out to 

  osullik [at] umd [dot] edu

  nsch [at] umd [dot] edu
