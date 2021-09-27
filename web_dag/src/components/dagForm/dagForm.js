import React, { useState, useRef } from 'react';
import classes from './dagForm.module.css';
import Button from '../UI/Button';
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
      <div className={classes.DagForm}>
        <h2 className={classes.h2}>Dag Creation </h2>
        <p>Here you can add your variables you lazy dagger</p>
        <form onSubmit={nodeHandler}>
          <div className={classes.inputDiv}>
            <input
              className={classes.input}
              type="text"
              id="cause"
              ref={causeRef}
            />{' '}
            <em>causes</em>{' '}
            <input
              className={classes.input}
              type="text"
              id="effect"
              ref={effRef}
            />
          </div>
          <div className={classes.inputBut}>
            <Button type="submit" className={classes.AddBut}>
              Add
            </Button>{' '}
            <Button onClick={emptyList} className={classes.DelBut}>
              X
            </Button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default DagForm;
