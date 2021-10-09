import React, { useState } from 'react';
import ELK from 'elkjs/lib/elk.bundled.js';
import Card from '@mui/material/Card';
import SvgGraph from './SvgGraph.js';
import Button from '@mui/material/Button';
import ShowChartIcon from '@mui/icons-material/ShowChart';
import Stack from '@mui/material/Stack';
import classes from './DagGraph.module.css';

const DagGraph = (props) => {
  const [isGraphReady, setIsGraphReady] = useState(false);
  const [graph, setGraph] = useState(props.item);

  async function drawGraph() {
    if (props.item.length === 0) {
      return;
    }
    const elk = new ELK();
    const graphEdges = props.item.map((node) => ({
      id: node.key,
      sources: [node.cause],
      targets: [node.effect],
    }));

    const causeArray = props.item.map((node) => node.cause);
    const effectArray = props.item.map((node) => node.effect);
    const unfilteredArray = causeArray.concat(effectArray);
    const nodesArray = [...new Set(unfilteredArray)];
    const graphForElk = {
      id: 'root',
      layoutOptions: {
        //      'elk.algorithm': 'mrtree',
        'elk.algorithm': 'layered',
        //      'elk.spacing.nodeNode': '20',
      },
      children: nodesArray.map((i) => ({ id: i, width: 6, height: 6 })),
      edges: graphEdges,
      edgesPoints: [],
    };
    const getMultiLinkData = (grafo) => {
      const multiLinkData = grafo.edges.map((edge) => ({
        source: [...edge.sources],
        target: [...edge.targets],
      }));
      // get x and y from props.graph.children and put it in multiLinkData
      multiLinkData.forEach((elem) => {
        const SourceEl = grafo.children.find((x) => x.id === elem.source[0]);
        const TargetEl = grafo.children.find((x) => x.id === elem.target[0]);
        elem.source = [SourceEl.x + 3, SourceEl.y];
        elem.target = [TargetEl.x - 3, TargetEl.y];
      });
      grafo.edgesPoints = multiLinkData;
      console.log('ho fatto multiLinkData');
    };
    let graphFromElk = await elk.layout(graphForElk);
    getMultiLinkData(graphFromElk);
    setGraph(graphFromElk);
    setIsGraphReady(true);
  }

  const clearGraph = () => {
    setIsGraphReady(false);
    setGraph(props.item);
  };

  return (
    <Card className={classes.DagGraph}>
      <h2 className={classes.h2}>Your Dag</h2>
      <Stack direction="row" className={classes.DagGraph} spacing={2}>
        <Button
          variant="contained"
          className={classes.button}
          onClick={drawGraph}
          startIcon={<ShowChartIcon />}
        >
          Draw
        </Button>
        {isGraphReady && (
          <Button variant="contained" onClick={clearGraph}>
            Clear
          </Button>
        )}
      </Stack>
      <br />
      {isGraphReady && <SvgGraph graph={graph} />}
    </Card>
  );
};

export default DagGraph;
