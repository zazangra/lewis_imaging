import React from 'react';
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import classes from './DagList.module.css';

const DagList = (props) => {
  return (
    <Card className={classes.DagList}>
      <Typography variant="h3" gutterBottom className={classes.h3}>
        Your Dag Items
      </Typography>
      <Typography variant="p" gutterBottom>
        Click an item to delete it
      </Typography>
      <ul className={classes.ul}>
        {' '}
        {props.item.map((node) => (
          <li
            key={node.key}
            className={classes.li}
            onClick={() => {
              props.removeItem(node.key);
            }}
          >
            {node.cause}
            <em> causes </em>
            {node.effect}
          </li>
        ))}
      </ul>
    </Card>
  );
};

export default DagList;

// attemp for tikz drawer; it probably isn't manageble
//
//import Button from '../UI/Button';
//  const lala = () => {
//    console.log(props.tikzItem);
//    let pream = `
//                <br>% minimal tikz preamble <br>
//                \\usepackage{pgf, tikz}
//                <br>\\usetikzlibrary{arrows, automata, chains, shapes, matrix}<br>
//                <br>%%%%%%%%%%%%%%%%%%%%%%%%%%%%<br>
//                <br>%%%%%%% here image code %%%%%%%<br>
//                <br>\\begin{figure}<br>
//                \\centering
//                <br>\\begin{tikzpicture}[->, >=stealth', shorten >= 1pt, auto,node distance =3cm,semithick]<br>
//                \\tikzstyle{every state}=[fill=gray!20,draw=black,text=black]
//                  `;
//
//    var tikzpage = window.open();
//    tikzpage.document.write(pream);
//  };
//      <Button onClick={lala}>lala</Button>
