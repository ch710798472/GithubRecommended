/**
 * Created by ch on 16-1-4.
 */
function show_china(){
    select=document.getElementById("china_rank");
    $(select).empty();
    var rankinfo  = $("<div id='rankinfo' style='margin-top:55px;color:blue;font-size: 40px;font-family: sans-serif;'><p align='center'>中国地区Github用户评分排名</p></div>");
    rankinfo.appendTo(select);
    var github_table  = $("<table class='table table-striped table-hover'>");
    github_table.appendTo(select);
    var head = $("<thead class='table_title'>");
    head.appendTo(github_table);
    var tr = $("<tr>");
    tr.appendTo(head);

    $("<th class='border_right wid1'>排名</th>").appendTo(tr);
    $("<th class='border_right wid1'>头像</th>").appendTo(tr);
    $("<th class='border_right wid1'>用户(姓名)</th>").appendTo(tr);
    //$("<th>评分</th>").appendTo(tr);
    //$("<th>擅长语言</th>").appendTo(tr);
    $("<th class='border_right wid1'>仓库数</th>").appendTo(tr);
    $("<th class='border_right wid1'>gist数</th>").appendTo(tr);
    $("<th class='border_right wid1'>公司</th>").appendTo(tr);
    $("<th class='border_right wid1'>博客</th>").appendTo(tr);
    //$("<th class='border_right wid1'>邮箱</th>").appendTo(tr);
    //$("<th>followers</th>").appendTo(tr);
    //$("<th>following</th>").appendTo(tr);
    $("<th class='border_right wid1'>开通时间</th>").appendTo(tr);
    $("<th class='border_right wid1'>更新时间</th>").appendTo(tr);
    $("<th class='border_right wid1'>地区</th>").appendTo(tr);


    $("<tbody class='tbody_color'>").appendTo(github_table);

    var tips;
    d3.json("/static/bootstrap/data/userMoreInfo.json", function(data) {
        for (var i in data) {
            //console.log(data[i]);
            tips = "followers:"+data[i]["followers"]+"  following:"+data[i]["following"];
            var tr = $("<tr class='media-tooltip' data-toggle='tooltip' data-html='true' data-original-title='<h3>"+tips+"</h3>' >");// onclick='fun()'
            tr.appendTo(github_table);
            var count = parseInt(i) + 1;
            if(data[i]["name"]==null)
                data[i]["name"]="无";
            if(data[i]["company"]==null)
                data[i]["company"]="无";
            if(data[i]["email"]==null)
                data[i]["email"]="无";
            if(data[i]["location"]==null)
                data[i]["location"]="无";
            if(data[i]["created_at"]==null)
                data[i]["created_at"]="无";
            if(data[i]["updated_at"]==null)
                data[i]["updated_at"]="无";
            $("<td>NO." + count + "</td>").appendTo(tr);
            $("<td>" + "<img height='48' width='48' src=" + data[i]["avatar_url"] + "/>" + "</td>").appendTo(tr);
            $("<td>" + "<a href='https://github.com/" + data[i]["login"] + "' target='_blank'>" + data[i]["login"] + "</a>" + "&nbsp(" + data[i]["name"] + ")"+ "</td>").appendTo(tr);
            //$("<td class='solid'>" + parseInt(data[i]["score"]) + "</td>").appendTo(tr);
            //$("<td class='solid'>" + data[i]["language"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["public_repos"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["public_gists"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["company"] + "</td>").appendTo(tr);
            if(data[i]["blog"]!=null)
                if(data[i]["blog"].length>20)
                    $("<td >" + "<a href='" + data[i]["blog"] + "' target='_blank'>"+data[i]["blog"].substr(0,20) + "...</a>").appendTo(tr);
                else
                    $("<td >" + "<a href='" + data[i]["blog"] + "' target='_blank'>"+data[i]["blog"] + "</a>").appendTo(tr);
            else
                $("<td >" + "无" +"</td>").appendTo(tr);
            //$("<td>" + data[i]["email"] + "</td>").appendTo(tr);
            //$("<td class='solid'>" + data[i]["followers"] + "</td>").appendTo(tr);
            //$("<td class='solid'>" + data[i]["following"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["created_at"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["updated_at"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["location"] + "</td>").appendTo(tr);
        }
        $(function () { $("[data-toggle='tooltip']").tooltip(); });
        //修改提示
        //$(".media-tooltip").tooltip('hide')
        //        .attr('data-original-title', "followers:"+data[i]["followers"]+"  following:"+data[i]["following"])
        //        .tooltip('fixTitle');

    });
}
//
//function fun(){
//    //console.log("1");
//}

function show_C(){
    select=document.getElementById("china_rank");
    $(select).empty();
    var rankinfo  = $("<div id='rankinfo' style='margin-top:55px;color:blue;font-size: 40px;font-family: sans-serif;'><p align='center'>中国地区Github C语言用户评分排名</p></div>");
    rankinfo.appendTo(select);
    var github_table  = $("<table class='table table-striped table-hover'>");
    github_table.appendTo(select);
    var head = $("<thead class='table_title'>");
    head.appendTo(github_table);
    var tr = $("<tr>");
    tr.appendTo(head);

    $("<th class='border_right wid1'>排名</th>").appendTo(tr);
    $("<th class='border_right wid1'>头像</th>").appendTo(tr);
    $("<th class='border_right wid1'>用户(姓名)</th>").appendTo(tr);
    //$("<th>评分</th>").appendTo(tr);
    //$("<th>擅长语言</th>").appendTo(tr);
    $("<th class='border_right wid1'>仓库数</th>").appendTo(tr);
    $("<th class='border_right wid1'>gist数</th>").appendTo(tr);
    $("<th class='border_right wid1'>公司</th>").appendTo(tr);
    $("<th class='border_right wid1'>博客</th>").appendTo(tr);
    //$("<th class='border_right wid1'>邮箱</th>").appendTo(tr);
    //$("<th>followers</th>").appendTo(tr);
    //$("<th>following</th>").appendTo(tr);
    $("<th class='border_right wid1'>开通时间</th>").appendTo(tr);
    $("<th class='border_right wid1'>更新时间</th>").appendTo(tr);
    $("<th class='border_right wid1'>地区</th>").appendTo(tr);


    $("<tbody class='tbody_color'>").appendTo(github_table);

    var tips;
    d3.json("/static/bootstrap/data/c_userMoreInfo.json", function(data) {
        for (var i in data) {
            //console.log(data[i]);
            tips = "followers:"+data[i]["followers"]+"  following:"+data[i]["following"];
            var tr = $("<tr class='media-tooltip' data-toggle='tooltip' data-html='true' data-original-title='<h3>"+tips+"</h3>' >");// onclick='fun()'
            tr.appendTo(github_table);
            var count = parseInt(i) + 1;
            if(data[i]["name"]==null)
                data[i]["name"]="无";
            if(data[i]["company"]==null)
                data[i]["company"]="无";
            if(data[i]["email"]==null)
                data[i]["email"]="无";
            if(data[i]["location"]==null)
                data[i]["location"]="无";
            if(data[i]["created_at"]==null)
                data[i]["created_at"]="无";
            if(data[i]["updated_at"]==null)
                data[i]["updated_at"]="无";
            $("<td>NO." + count + "</td>").appendTo(tr);
            $("<td>" + "<img height='48' width='48' src=" + data[i]["avatar_url"] + "/>" + "</td>").appendTo(tr);
            $("<td>" + "<a href='https://github.com/" + data[i]["login"] + "' target='_blank'>" + data[i]["login"] + "</a>" + "&nbsp(" + data[i]["name"] + ")"+ "</td>").appendTo(tr);
            //$("<td class='solid'>" + parseInt(data[i]["score"]) + "</td>").appendTo(tr);
            //$("<td class='solid'>" + data[i]["language"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["public_repos"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["public_gists"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["company"] + "</td>").appendTo(tr);
            if(data[i]["blog"]!=null)
                if(data[i]["blog"].length>20)
                    $("<td >" + "<a href='" + data[i]["blog"] + "' target='_blank'>"+data[i]["blog"].substr(0,20) + "...</a>").appendTo(tr);
                else
                    $("<td >" + "<a href='" + data[i]["blog"] + "' target='_blank'>"+data[i]["blog"] + "</a>").appendTo(tr);
            else
                $("<td >" + "无" +"</td>").appendTo(tr);
            //$("<td>" + data[i]["email"] + "</td>").appendTo(tr);
            //$("<td class='solid'>" + data[i]["followers"] + "</td>").appendTo(tr);
            //$("<td class='solid'>" + data[i]["following"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["created_at"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["updated_at"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["location"] + "</td>").appendTo(tr);
        }
        $(function () { $("[data-toggle='tooltip']").tooltip(); });
        //修改提示
        //$(".media-tooltip").tooltip('hide')
        //        .attr('data-original-title', "followers:"+data[i]["followers"]+"  following:"+data[i]["following"])
        //        .tooltip('fixTitle');

    });
}

function show_python(){
    select=document.getElementById("china_rank");
    $(select).empty();
    var rankinfo  = $("<div id='rankinfo' style='margin-top:55px;color:blue;font-size: 40px;font-family: sans-serif;'><p align='center'>中国地区Github python语言用户评分排名</p></div>");
    rankinfo.appendTo(select);
    var github_table  = $("<table class='table table-striped table-hover'>");
    github_table.appendTo(select);
    var head = $("<thead class='table_title'>");
    head.appendTo(github_table);
    var tr = $("<tr>");
    tr.appendTo(head);

    $("<th class='border_right wid1'>排名</th>").appendTo(tr);
    $("<th class='border_right wid1'>头像</th>").appendTo(tr);
    $("<th class='border_right wid1'>用户(姓名)</th>").appendTo(tr);
    //$("<th>评分</th>").appendTo(tr);
    //$("<th>擅长语言</th>").appendTo(tr);
    $("<th class='border_right wid1'>仓库数</th>").appendTo(tr);
    $("<th class='border_right wid1'>gist数</th>").appendTo(tr);
    $("<th class='border_right wid1'>公司</th>").appendTo(tr);
    $("<th class='border_right wid1'>博客</th>").appendTo(tr);
    //$("<th class='border_right wid1'>邮箱</th>").appendTo(tr);
    //$("<th>followers</th>").appendTo(tr);
    //$("<th>following</th>").appendTo(tr);
    $("<th class='border_right wid1'>开通时间</th>").appendTo(tr);
    $("<th class='border_right wid1'>更新时间</th>").appendTo(tr);
    $("<th class='border_right wid1'>地区</th>").appendTo(tr);


    $("<tbody class='tbody_color'>").appendTo(github_table);

    var tips;
    d3.json("/static/bootstrap/data/py_userMoreInfo.json", function(data) {
        for (var i in data) {
            //console.log(data[i]);
            tips = "followers:"+data[i]["followers"]+"  following:"+data[i]["following"];
            var tr = $("<tr class='media-tooltip' data-toggle='tooltip' data-html='true' data-original-title='<h3>"+tips+"</h3>' >");// onclick='fun()'
            tr.appendTo(github_table);
            var count = parseInt(i) + 1;
            if(data[i]["name"]==null)
                data[i]["name"]="无";
            if(data[i]["company"]==null)
                data[i]["company"]="无";
            if(data[i]["email"]==null)
                data[i]["email"]="无";
            if(data[i]["location"]==null)
                data[i]["location"]="无";
            if(data[i]["created_at"]==null)
                data[i]["created_at"]="无";
            if(data[i]["updated_at"]==null)
                data[i]["updated_at"]="无";
            $("<td>NO." + count + "</td>").appendTo(tr);
            $("<td>" + "<img height='48' width='48' src=" + data[i]["avatar_url"] + "/>" + "</td>").appendTo(tr);
            $("<td>" + "<a href='https://github.com/" + data[i]["login"] + "' target='_blank'>" + data[i]["login"] + "</a>" + "&nbsp(" + data[i]["name"] + ")"+ "</td>").appendTo(tr);
            //$("<td class='solid'>" + parseInt(data[i]["score"]) + "</td>").appendTo(tr);
            //$("<td class='solid'>" + data[i]["language"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["public_repos"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["public_gists"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["company"] + "</td>").appendTo(tr);
            if(data[i]["blog"]!=null)
                if(data[i]["blog"].length>20)
                    $("<td >" + "<a href='" + data[i]["blog"] + "' target='_blank'>"+data[i]["blog"].substr(0,20) + "...</a>").appendTo(tr);
                else
                    $("<td >" + "<a href='" + data[i]["blog"] + "' target='_blank'>"+data[i]["blog"] + "</a>").appendTo(tr);
            else
                $("<td >" + "无" +"</td>").appendTo(tr);
            //$("<td>" + data[i]["email"] + "</td>").appendTo(tr);
            //$("<td class='solid'>" + data[i]["followers"] + "</td>").appendTo(tr);
            //$("<td class='solid'>" + data[i]["following"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["created_at"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["updated_at"] + "</td>").appendTo(tr);
            $("<td>" + data[i]["location"] + "</td>").appendTo(tr);
        }
        $(function () { $("[data-toggle='tooltip']").tooltip(); });
        //修改提示
        //$(".media-tooltip").tooltip('hide')
        //        .attr('data-original-title', "followers:"+data[i]["followers"]+"  following:"+data[i]["following"])
        //        .tooltip('fixTitle');

    });
}