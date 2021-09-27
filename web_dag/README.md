# DAGproject

## Single web page project, allowing getting a .svg DAG from variable imputs 

The idea is very simple, there is no need to add specification to this title. Plus, this directory is currently private, so that every one is  concerned  
already knows what's going on.

This read me is for a todo list  and a "what we already have" list. If the directory will be published, this will be the first thing to modify.

-New Feature Requeste: output for latex tikz graph

-Big Change: the entire project has been moved to React! It was unfeasible for vanilla javascript! (I will cancel all previous files and leave only src/ public/
and the package.json ... contact me for help with the installation)

### TODOs

The list here is not in order, nor is smart designed

- Add button x function in <DagForm> (empty the list)
- Add graph layer (probably, https://github.com/kieler/elkjs)
- Add graph render (https://github.com/eclipse/sprotty or any other)


- avoid autocausation for n>2 ntuples (somehow, js will have to learn to see directed paths & co)


-New Feature Requeste: output for latex tikz graph
    - implement button and component
    - Find a way to let js decide which is [right of]
    - Cicle through allCause and allEffect 

  Last Update (2/9/2021)

### DONE

The list is correctly rendered and you can delete each item. There are also checks for empty inputs, autocausation and equal inputs.

#### If you're cloning this, do not rely too much on this md, it surely won't be updated!
#### If you're pushing something, please modify this (Lorenzo is the laziest)!!!!
#### Forza Toro!!
