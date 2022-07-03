const urls = [pieChartDataUrl];

Promise.all(urls.map(url => d3.json(url))).then(run);

function run(dataset) {
   d3PieChart(dataset[0], dataset[1]);
};
