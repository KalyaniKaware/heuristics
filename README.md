[![Codespaces Prebuilds](https://github.com/nogibjj/heuristics/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/nogibjj/heuristics/actions/workflows/codespaces/create_codespaces_prebuilds)
[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/heuristics/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/heuristics/actions/workflows/main.yml)


# Kalyani's additions:
1. Add a shebang line to use cli
2. use chmod +x file_name.py to make the file a command line function

`./file_name.py —help` — should be successful
`chmod +x file_name.py` — to add permissions 
```
(base) MacBook-Pro:heuristics kalyani$ ./my_greedy_coin_using_copilot.py --help
bash: ./my_greedy_coin_using_copilot.py: Permission denied
(base) MacBook-Pro:heuristics kalyani$ chmod +x my_greedy_coin_using_copilot.py
(base) MacBook-Pro:heuristics kalyani$ ./my_greedy_coin_using_copilot.py --help
Usage: my_greedy_coin_using_copilot.py [OPTIONS] COMMAND [ARGS]...

  Return the minimum number of coins for a given change Example:
  ./my_greedy_coin_using_copilot.py 0.99

Options:
  --help  Show this message and exit.

Commands:
  dd  Return the minimum number of coins for a given change Example:...
  dq  Return the minimum number of coins for a given change Example:...
(base) MacBook-Pro:heuristics kalyani$ ./my_greedy_coin_using_copilot.py dq 0.99
Your change for 0.99: 
3 quarter
2 dime
(base) MacBook-Pro:heuristics kalyani$ ./my_greedy_coin_using_copilot.py dd 0.99
Your change for 0.99: 
9 dime
```

# Advanced-Heuristics-and-Algorithms-in-Python
Copilot assisted algorithms and heuristics

## Parallel

Information on [CUDA with Numba](https://numba.pydata.org/numba-doc/latest/cuda/)
For using CUDA you must create an activate conda:  

```
conda create
conda create --name myenv
conda activate myenv
conda init bash
```

## Probability

* Roulette simulator:

`python probability/roulette.py spin --count 10000 --color="black"`

* Poker similator (run `make install` then)

`python probability/poker.py interactive --rounds 5`


## Algorithms

* dijkstra shortest path
* merge sort

## Equations

### David Sumpter's 10 Equations

* Judgment Equation:  Bayes
* Betting Equation
* Confidence Equation
* Skill Equation:  Markov
* Influencer Equation
* Market Equation
* Advertising Equation
* Reward Equation
* Learning Equation
* Universal Equation


## Week 2 algo translations 

* Using advanced features of copilot labs to translate algo

### Languages installed via .devcontainer and verified can translate

* Ruby
* Rust


## Week 1

* [command-line tool that accepts arbitrary cities and finds shortest path using greedy random similuations](https://github.com/nogibjj/heuristics/blob/main/fetch_cities_lat_long.py)
* [greedy coin cli](https://github.com/nogibjj/heuristics/blob/main/greedy_coin.py)


## Research Topic to Explore in Future

* [Outlier Detection](https://github.com/yzhao062/pyod)
* Predator/Prey
* Evalutionary Algorithms


## References

* [Ten Equations](https://www.amazon.com/Ten-Equations-that-Rule-World-ebook/dp/B07Z78T7WJ)
* [MIT intro algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_prob1/)



