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

## Recompiling the paper from tex:

### Setting up compilation environment for MacOS: 

1. Download [Homebrew](brew.sh): 

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. Install TexLive: 

        brew install texlive

3. Install Inkscape

        brew install --cask inkscape

4. (If it isn't on your machine by default) GNU Make

        brew install make

### Setting up compilation environment For Windows: 

1. Run Powershell as administrator: 

2. Install [Chocolatey](https://chocolatey.org/): 

        Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

3. Install GNU Make: 

        choco install Make

4. Install Perl (for LatexMk)

        choco install strawberryperl

5. Install Ruby (for Editing Scripts)

        choco install ruby

6. Install TexLive Utilites: 

        choco install texlive

7. Install MiKTeX: 

        choco install miktex

8. Install LatexMK with MikTex Package Manager (through GUI)

9. Install InkScape

        choco install inkscape


### Key commands for Making the file: 

To compile the PDF, simply run the following from the root of the project directory:

    make compass.pdf

You'll notice a lot of random intermediary files get made. To get rid of them and leave your PDF use:

    make publish

Sometimes everything goes wrong and we need to start again, when that happens use: 

    make clean

The [scripts](https://github.com/osullik/COMPASS_GEOSEARCH/tree/main/scripts) directory contains a collection of scripts taken from [Jordan Boyd-Graber](https://github.com/Pinafore/publications/tree/master/scripts) that are useful for editing and checking. Github tends to mess with the permissions on these, so you'll likely need to CHMOD them back to be executable again. The *make main.pdf* command uses some of these scripts, so it is a good idea to do that occasionally. 

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
