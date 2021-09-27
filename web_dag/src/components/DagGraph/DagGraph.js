import React, { useState, useEffect } from 'react';
import SvgGraph from './SvgGraph.js';
import Button from '../UI/Button.js';
import classes from './DagGraph.module.css';

const DagGraph = (props) => {
  const [isClicked, setIsClicked] = useState(false);
  const [isGraphReady, setIsGraphready] = useState(false);

  const drawGraph = () => {
    setIsClicked(true);
    if (props.item.children.length > 0) {
      setIsGraphready(true);
    } else {
      setIsGraphready(false);
    }
  };

  useEffect(() => {
    setIsClicked(false);
  }, [props.item]);

  return (
    <div className={classes.DagGraph}>
      <h2 className={classes.h2}>Your Dag</h2>
      <Button className={classes.button} onClick={drawGraph}>
        Draw
      </Button>
      {isClicked
        ? isGraphReady && <SvgGraph graph={props.item} isClicked={isClicked} />
        : null}
    </div>
  );
};

export default DagGraph;
