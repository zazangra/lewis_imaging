import React, { useState } from 'react';
import classes from './App.css';
import DagForm from './components/dagForm/dagForm';
import DagList from './components/DagList/DagList';
import ModalError from './components/UI/ModalError';
import DagGraph from './components/DagGraph/DagGraph';
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';

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
        <Card className="dag-intro">
          <Typography
            variant="h2"
            className={classes.h2}
            component="div"
            gutterBottom
          >
            Causal Dag Creator
          </Typography>
          <Typography variant="p" gutterBottom>
            Some sort of intro may be put here
          </Typography>
        </Card>
        <DagForm addNode={takeNode} clearList={clearList} />
        <DagList item={nodeList} removeItem={delNode} />
        <DagGraph
          item={nodeList}
          isGraphClicked={isGraphClicked}
          changeIsGraphClicked={changeIsGraphClicked}
        />
      </div>
    </div>
  );
}

export default App;
