import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const Chart = ({ data }) => {
    const chartRef = useRef();

    useEffect(() => {
        const svg = d3.select(chartRef.current)
            .attr('width', 500)
            .attr('height', 300);

        svg.selectAll('*').remove();  // Clean chart before rendering

        svg.selectAll('rect')
            .data(data)
            .enter()
            .append('rect')
            .attr('x', (d, i) => i * 25)
            .attr('y', d => 300 - d)
            .attr('width', 20)
            .attr('height', d => d)
            .attr('fill', 'blue');
    }, [data]);

    return <svg ref={chartRef}></svg>;
};

export default Chart;
