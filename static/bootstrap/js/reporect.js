function reporect(){
    var w = 600;
    var h = 300;
    var barPadding = 1;
    //矩形之间的空白
    var rectPadding = 4;
    var svg = d3.select("body").append("svg");
    svg.attr("width", w)
        .attr("height", h)
        .attr("class","svgmargin")
        .attr("id","svg1");
    var dataset = [];
    var datalebel = [];
    var maxValue = 100;
    //画布周边的空白
    var padding = {left:30, right:30, top:20, bottom:20};

    d3.json("/static/bootstrap/data/1.1.rect", function(json) {
        i = 0;
        for (var key in json) {
//                console.log(d[key]);
            datalebel[i] = json[key][0];
            dataset[i++] = json[key][1];
        }

        //x轴的比例尺
        var xScale = d3.scale.ordinal()
            .domain(d3.range(dataset.length))
            .rangeRoundBands([0, w - padding.left - padding.right]);

        //y轴的比例尺
        var yScale = d3.scale.linear()
            .domain([0,d3.max(dataset)])
            .range([h - padding.top - padding.bottom, 0]);

        //定义x轴
        var xAxis = d3.svg.axis()
                .scale(xScale)
                .orient("bottom")
//                    .tickFormat(function(d,j) { return datalebel[j]; })
            ;//自定义横坐标刻度说明

        //定义y轴
        var yAxis = d3.svg.axis()
            .scale(yScale)
            .orient("left");

        //添加矩形元素
        var rects = svg.selectAll(".linerect")
            .data(dataset)
            .enter()
            .append("rect")
            .attr("class","lineRect")
            .attr("transform","translate(" + padding.left + "," + padding.top + ")")
            .attr("x", function(d,i){
                return xScale(i) + rectPadding/2;
            } )
            .attr("width", xScale.rangeBand() - rectPadding )
            .attr("y",function(d){
                var min = yScale.domain()[0];
                return yScale(min);
            })
            .attr("height", function(d){
                return 0;
            })
            .transition()
            .delay(function(d,i){
                return i * 200;
            })
            .duration(2000)
            .ease("bounce")
            .attr("y",function(d){
                return yScale(d);
            })
            .attr("height", function(d){
                return h - padding.top - padding.bottom - yScale(d);
            });

        d3.selectAll("rect")
            .on("click", function() {
                sortBars();
            })
            .append("title")
            .text(function(d,j) {
                return "仓库：" + datalebel[j];
            });

        var sortOrder = false;
        var sortBars = function() {
            sortOrder = !sortOrder;
            //改变矩形位置，平移
            svg.selectAll("rect")
                .sort(function(a, b) {
                    if (sortOrder) {
                        return d3.ascending(a, b);
                    } else {
                        return d3.descending(a, b);
                    }
                })
                .transition()
                .delay(function(d, i) {
                    return i * 50;
                })
                .duration(1000)
                .ease("bounce")
                .attr("x", function(d, i) {
                    return xScale(i);
                });
            //改变标签位置，平移
            svg.selectAll(".rectText")
                .sort(function(a, b) {
                    if (sortOrder) {
                        return d3.ascending(a, b);
                    } else {
                        return d3.descending(a, b);
                    }
                })
                .transition()
                .delay(function(d,i){
                    return i * 100;
                })
                .duration(1000)
                .ease("bounce")
                .attr("x", function(d,i){
                    return xScale(i);
                });

        };

        //添加文字元素
        var texts = svg.selectAll(".rectText")
            .data(dataset)
            .enter()
            .append("text")
            .attr("class","rectText")
            .attr("transform","translate(" + padding.left + "," + padding.top + ")")
            .attr("x", function(d,i){
                return xScale(i) + rectPadding/2;
            } )
            .attr("dx",function(){
                return (xScale.rangeBand() - rectPadding)/2;
            })
            .attr("dy",function(d){
                return 20;
            })
            .text(function(d){
                return d;
            })
            .attr("y",function(d){
                var min = yScale.domain()[0];
                return yScale(min);
            })
            .transition()
            .delay(function(d,i){
                return i * 200;
            })
            .duration(2000)
            .ease("bounce")
            .attr("y",function(d){
                return yScale(d);
            });

        //添加x轴
        svg.append("g")
            .attr("class","xaxis")
            .attr("transform","translate(" + padding.left + "," + (h - padding.bottom) + ")")
            .call(xAxis);

        //添加y轴
        svg.append("g")
            .attr("class","yaxis")
            .attr("transform","translate(" + padding.left + "," + padding.top + ")")
            .call(yAxis);
        //改变x轴的刻度文字竖排显示
//            svg.selectAll("g.tick.text")   //add label for x axis
//////                    .attr("text-anchor", "end")
//                    .style({"writing-mode":"tb-rl"})
////                    .attr("y", function(d){
////                        return 30;
////                    })
//            ;

        //添加文字排序说明
        var svg1 = d3.select("body").append("svg");
        svg1.attr("width", 200)
            .attr("height", 300)
            .attr("class","svgmargin")
            .attr("id","svg1.1");
        var texts = svg1.selectAll(".externText")
            .data(dataset)
            .enter()
            .append("text")
            .attr("class","externText")
            .attr("transform","translate(" + padding.left + "," + padding.top + ")")
            .transition()
            .delay(function(d,i){
                return i * 200;
            })
            .duration(2000)
            .ease("bounce")
            .attr("x", function(d,i){
                return 0;
            } )
            .attr("dx",function(){
                return 10;
            })
            .attr("dy",function(d){
                return 30;
            })
            .text(function(d,j){
                return (j+1)+": "+datalebel[j] + " " + dataset[j];
            })
            .attr("y",function(d,j){
                return 25*j;
            });
    });
}