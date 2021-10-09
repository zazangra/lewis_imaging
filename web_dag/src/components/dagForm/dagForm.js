import React, { useState, useRef } from 'react';
import classes from './dagForm.module.css';
import Button from '@mui/material/Button';
import AddIcon from '@mui/icons-material/Add';
import Stack from '@mui/material/Stack';
import ClearAllIcon from '@mui/icons-material/ClearAll';
import TextField from '@mui/material/TextField';
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import ModalError from '../UI/ModalError';

const DagForm = (props) => {
  const [error, setError] = useState();

  const causeRef = useRef();
  const effRef = useRef();

  const nodeHandler = (event) => {
    event.preventDefault();
    const nodeObj = {
      cause: causeRef.current.value,
      effect: effRef.current.value,
      key:
        Math.random().toString() +
        causeRef.current.value +
        effRef.current.value,
    };
    if (nodeObj.cause.length === 0 || nodeObj.effect.length === 0) {
      setError({
        title: 'Invalid Input',
        message: 'Please do not leave empty input',
      });
      return;
    }
    if (nodeObj.cause === nodeObj.effect) {
      setError({
        title: 'Invalid Input',
        message: 'There is no way I will allow autocausation',
      });
      return;
    }
    props.addNode(nodeObj);
    causeRef.current.value = '';
    effRef.current.value = '';
  };
  const errorHandler = () => {
    setError(null);
  };
  const emptyList = () => {
    props.clearList();
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
      <Card className={classes.DagForm}>
        <Typography variant="h3" gutterBottom className={classes.h2}>
          Dag Creation
        </Typography>
        <Typography variant="p">
          Here you can add your variables you lazy dagger
        </Typography>
        <form onSubmit={nodeHandler}>
          <Stack
            direction="row"
            spacing={2}
            justifyContent="center"
            alignItems="center"
            className={classes.inputDiv}
          >
            <TextField
              label="Cause"
              type="text"
              id="cause"
              variant="outlined"
              inputRef={causeRef}
              size="string"
            />
            <TextField
              label="Effect"
              type="text"
              id="effect"
              variant="outlined"
              inputRef={effRef}
              size="string"
            />
          </Stack>
          <Stack
            direction="row"
            spacing={2}
            justifyContent="center"
            alignItems="center"
          >
            <Button
              variant="contained"
              type="submit"
              className={classes.AddBut}
              startIcon={<AddIcon />}
            >
              Add
            </Button>
            <Button
              variant="contained"
              onClick={emptyList}
              className={classes.DelBut}
              startIcon={<ClearAllIcon />}
            >
              Clear All
            </Button>
          </Stack>
        </form>
      </Card>
    </div>
  );
};

export default DagForm;
