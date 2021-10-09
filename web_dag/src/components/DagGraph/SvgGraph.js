import React, { useRef, useEffect } from 'react';
import Button from '@mui/material/Button';
import DownloadIcon from '@mui/icons-material/Download';
import classes from './SvgGraph.module.css';
import * as d3 from 'd3';
import downloadSvg from 'svg-crowbar';

const SvgGraph = (props) => {
  const ref = useRef();

  const handleCD = () => {
    downloadSvg(ref.current);
  };

  useEffect(() => {
    const link = d3.linkHorizontal();
    const svgElement = d3.select(ref.current);
    svgElement
      .selectAll('path')
      .data(props.graph.edgesPoints)
      .join('path')
      .attr('d', link)
      .attr('stroke', '#213f20')
      .attr('stroke-width', '0.1px')
      .attr('fill', 'none')
      .attr('marker-end', 'url(#arrowhead)');
  }, [props.isClicked, props.graph.edgesPoints]);

  return (
    <div className={classes.box}>
      <svg
        style={{ border: '0.5px solid black' }}
        xmlns="http://www.w3.org/2000/svg"
        width="95%"
        height="90%"
        viewBox="-20 0 150 80"
        ref={ref}
      >
        <defs>
          <marker
            id="arrowhead"
            markerWidth="10"
            markerHeight="10"
            refX="9"
            refY="5"
            orient="auto"
          >
            <polyline
              fill="none"
              stroke="#231f20"
              strokeWidth="3px"
              points="1 1, 7 5, 1 9"
            />
          </marker>
        </defs>
        <g fill="#61DAFB"></g>
        {props.graph.children.map((circle) => (
          <circle
            key={circle.id}
            cx={circle.x}
            cy={circle.y}
            text={circle.id}
            r={3}
            fill="#e09182"
            stroke="#a84432"
            strokeWidth="0.5px"
          ></circle>
        ))}
        {props.graph.children.map((text) => (
          <text
            textAnchor="middle"
            fill="solid black"
            key={text.id + Math.random().toString()}
            x={text.x}
            y={isNaN(text.y) ? text.y : text.y + 1}
            text={text.id}
            fontSize="3px"
          >
            {text.id}
          </text>
        ))}
      </svg>
      <div>
        <Button
          onClick={handleCD}
          variant="contained"
          startIcon={<DownloadIcon />}
          className={classes.button}
        >
          Download
        </Button>
      </div>
    </div>
  );
};

export default SvgGraph;
