import React, { useState, useEffect, useMemo } from 'react';
import './App.css';
import ELK from 'elkjs/lib/elk.bundled.js';
import DagForm from './components/dagForm/dagForm';
import DagList from './components/DagList/DagList';
import ModalError from './components/UI/ModalError';
import DagGraph from './components/DagGraph/DagGraph';

function App() {
  const [nodeList, setNodeList] = useState([]);
  const [error, setError] = useState();
  const [isGraphClicked, setIsGraphClicked] = useState(false);

  const changeIsGraphClicked = () => {
    setIsGraphClicked(true);
  };

  const takeNode = (nodeObj) => {
    if (
      nodeList.some(
        (i) => i.cause === nodeObj.cause && i.effect === nodeObj.effect
      )
    ) {
      setError({
        title: 'Invalid Input',
        message: 'Current node was alread inserted',
      });
      return;
    }
    setNodeList((nodeList) => {
      return [...nodeList, nodeObj];
    });
  };

  const delNode = (key) => {
    const newList = nodeList.filter((item) => item.key !== key);
    setNodeList(newList);
  };

  const errorHandler = () => {
    setError(null);
  };

  const clearList = () => {
    setNodeList([]);
  };

  let graph;
  graph = useMemo(() => {
    const graphEdges = nodeList.map((node) => ({
      id: node.key,
      sources: [node.cause],
      targets: [node.effect],
    }));

    const causeArray = nodeList.map((node) => node.cause);
    const effectArray = nodeList.map((node) => node.effect);
    const unfilteredArray = causeArray.concat(effectArray);
    const nodesArray = [...new Set(unfilteredArray)];
    return {
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
  }, [nodeList]);

  // draw coordinates for our nodes (after elk's calculations)
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
    console.log('ho fatto multiLinkData in memo');
  };

  useEffect(() => {
    const elk = new ELK();
    elk.layout(graph).then(getMultiLinkData);
    console.log('ho fatto elk e multiLinkData');
  }, [nodeList, graph]);

  return (
    <div>
      {error && (
        <ModalError
          title={error.title}
          message={error.message}
          onConfirm={errorHandler}
        />
      )}
      <div>
        <div className="dag-intro">
          <header className="dag-header">
            <h1> DAG CREATOR</h1>
          </header>
          <h2>Direct Acyclic Graphs</h2>
          <p> Some sort of DAG introduction may be put here (max 2 par) </p>
        </div>
        <DagForm addNode={takeNode} clearList={clearList} />
        <DagList item={nodeList} removeItem={delNode} />
        <DagGraph
          item={graph}
          isGraphClicked={isGraphClicked}
          changeIsGraphClicked={changeIsGraphClicked}
        />
      </div>
    </div>
  );
}

export default App;

//tikzItem={graph}
