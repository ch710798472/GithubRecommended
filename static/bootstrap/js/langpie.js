function langpie(){
    var dataset = new Array();//存储数据
    var datalebel = new Array();//存储标签
    var color = d3.scale.category10();
    var pie = d3.layout.pie();
    var w = 800;
    var h = 400;
    var outerRadius = 300 / 2;
    var innerRadius = 0;
    var arc = d3.svg.arc()
        .innerRadius(innerRadius)
        .outerRadius(outerRadius);
    var svg = d3.select("body")
        .append("svg")
        .attr("width", w)
        .attr("height", h)
        .attr("class","svgmargin")
        .attr("id","svg3");
    var i;
    d3.json("/static/bootstrap/data/repo_lang.json", function(json) {
//            console.log(d);
        i = 0;
        for(var key in json){
//                console.log(d[key]);
            datalebel[i] = json[key];
            dataset[i++] = json[key][1];
        }

        var piedata = pie(dataset);

        //可移动的饼状图
        var gAll = svg.append("g")//圆心
            .attr("transform","translate("　+　w/2　+　","　+h/2　+　")");
        var drag = d3.behavior.drag()
            .origin(function(d) { return d; })
            .on("drag", dragmove);

        var arcs = gAll.selectAll("g.arc")
            .data(piedata)
            .enter()
            .append("g")
//                    .attr("class", "arc")
//                    .attr("transform", "translate(" + outerRadius + ", " + outerRadius + ")")
            .each(function(d){
                //指定当前区域的平移量
                d.dx = 0;
                d.dy = 0;
                var padding = 0.01;	//空白大小
                d.startAngle += padding;
                d.endAngle -= padding;
            })
            .on("mouseover",function(d,i){
                //鼠标移过提示
//                        console.log(arc.centroid());
                var xPosition = w/2 - 250;
                var yPosition = h/2 - 50;
                svg.append("text")
                    .attr("id", "linktip")
                    .attr("x", xPosition)
                    .attr("y", yPosition)
                    .attr("text-anchor", "middle")
                    .attr("font-family", "sans-serif")
                    .attr("font-size", "30px")
                    .attr("font-weight", "bold")
                    .attr("fill", "black")
                    .text(function(d) {
//                                    console.log(datalebel[i][0])
                        return datalebel[i][0]+ ":" + datalebel[i][1];
                    });
            })
            .on("mouseout",function(d){
                //鼠标移除隐去提示
                d3.select("#linktip").remove();
            })
            .on("dblclick",function(d,i){
                //双击节点回到原始位置
                d3.select(this)
                    .attr("transform","translate("　+ 0　+　","　+ 0　+　")");
                d.dx = 0;//偏移量清零
                d.dy = 0;
            })
            .call(drag);

        arcs.append("path")
            .transition()
            .delay(function(d,i){
                return i * 200;
            })
            .duration(1000)
            .ease("bounce")
            .attr("fill", function(d, i) {
                return color(i);
            })
            .attr("d", arc);

        arcs.append("text")
            .transition()
            .delay(function(d,i){
                return i * 200;
            })
            .duration(1200)
            .ease("bounce")//elastic circle linear bounce
            .attr("transform", function(d) {
                return "translate(" + arc.centroid(d) + ")";
            })
            .attr("text-anchor", "middle")
            .attr("font-size", "16px")
            .text(function(d,i) {
                return datalebel[i][0];
            });

        function dragmove(d) {
            d.dx += d3.event.dx;
            d.dy += d3.event.dy;
            d3.select(this)
                .attr("transform","translate("+d.dx+","+d.dy+")");
        }

    });
}
function startpie(){
    var dataset = new Array();//存储数据
    var datalebel = new Array();//存储标签
    var color = d3.scale.category10();
    var pie = d3.layout.pie();
    var w = 800;
    var h = 400;
    var outerRadius = 300 / 2;
    var innerRadius = 0;
    var arc = d3.svg.arc()
        .innerRadius(innerRadius)
        .outerRadius(outerRadius);
    var svg = d3.select("body")
        .append("svg")
        .attr("width", w)
        .attr("height", h)
        .attr("class","svgmargin")
        .attr("id","svg3");
    var i;
    d3.json("/static/bootstrap/data/1.1.pie", function(json) {
//            console.log(d);
        i = 0;
        for(var key in json){
//                console.log(d[key]);
            datalebel[i] = json[key];
            dataset[i++] = json[key][1];
        }

        var piedata = pie(dataset);

        //可移动的饼状图
        var gAll = svg.append("g")//圆心
            .attr("transform","translate("　+　w/2　+　","　+h/2　+　")");
        var drag = d3.behavior.drag()
            .origin(function(d) { return d; })
            .on("drag", dragmove);

        var arcs = gAll.selectAll("g.arc")
            .data(piedata)
            .enter()
            .append("g")
//                    .attr("class", "arc")
//                    .attr("transform", "translate(" + outerRadius + ", " + outerRadius + ")")
            .each(function(d){
                //指定当前区域的平移量
                d.dx = 0;
                d.dy = 0;
                var padding = 0.01;	//空白大小
                d.startAngle += padding;
                d.endAngle -= padding;
            })
            .on("mouseover",function(d,i){
                //鼠标移过提示
//                        console.log(arc.centroid());
                var xPosition = w/2 - 250;
                var yPosition = h/2 - 50;
                svg.append("text")
                    .attr("id", "linktip")
                    .attr("x", xPosition)
                    .attr("y", yPosition)
                    .attr("text-anchor", "middle")
                    .attr("font-family", "sans-serif")
                    .attr("font-size", "30px")
                    .attr("font-weight", "bold")
                    .attr("fill", "black")
                    .text(function(d) {
//                                    console.log(datalebel[i][0])
                        return datalebel[i][0]+ ":" + datalebel[i][1];
                    });
            })
            .on("mouseout",function(d){
                //鼠标移除隐去提示
                d3.select("#linktip").remove();
            })
            .on("dblclick",function(d,i){
                //双击节点回到原始位置
                d3.select(this)
                    .attr("transform","translate("　+ 0　+　","　+ 0　+　")");
                d.dx = 0;//偏移量清零
                d.dy = 0;
            })
            .call(drag);

        arcs.append("path")
            .transition()
            .delay(function(d,i){
                return i * 200;
            })
            .duration(1000)
            .ease("bounce")
            .attr("fill", function(d, i) {
                return color(i);
            })
            .attr("d", arc);

        arcs.append("text")
            .transition()
            .delay(function(d,i){
                return i * 200;
            })
            .duration(1200)
            .ease("bounce")//elastic circle linear bounce
            .attr("transform", function(d) {
                return "translate(" + arc.centroid(d) + ")";
            })
            .attr("text-anchor", "middle")
            .attr("font-size", "16px")
            .text(function(d,i) {
                return datalebel[i][0];
            });

        function dragmove(d) {
            d.dx += d3.event.dx;
            d.dy += d3.event.dy;
            d3.select(this)
                .attr("transform","translate("+d.dx+","+d.dy+")");
        }

    });
}