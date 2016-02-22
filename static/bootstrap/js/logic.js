/**
 * Created by ch on 16-1-3.
 */
//响应不同的请求函数
function devild(i){
    if(document.getElementById("svg1") != null)
        document.body.removeChild(document.getElementById("svg1"));
    if(document.getElementById("svg1.1")!= null)
        document.body.removeChild(document.getElementById("svg1.1"));
    if(document.getElementById("svg2") != null)
        document.body.removeChild(document.getElementById("svg2"));
    if(document.getElementById("svg3") != null)
        document.body.removeChild(document.getElementById("svg3"));
    if(document.getElementById("svg4") != null)
        document.body.removeChild(document.getElementById("svg4"));
    if(document.getElementById("myCarousel") != null)
        document.getElementById("myCarousel").style.display="none";
    if(document.getElementById("insertImages") != null)
        document.getElementById("insertImages").style.display="none";
    if(document.getElementById("china_rank") != null)
        document.getElementById("china_rank").style.display="none";
    if(i ==1) {
        reporect();
    }
    if(i ==2) {
        langpie();
    }
    if(i ==3) {
        langpie();
    }
    if(i ==4) {
        networkx();
    }
}

function getstart(){
    if(document.getElementById("myCarousel").style.display == "none") {
        document.getElementById("myCarousel").style.display = "block";
        if(document.getElementById("svg1") != null)
            document.body.removeChild(document.getElementById("svg1"));
        if(document.getElementById("svg1.1")!= null)
            document.body.removeChild(document.getElementById("svg1.1"));
        if(document.getElementById("svg2") != null)
            document.body.removeChild(document.getElementById("svg2"));
        if(document.getElementById("svg3") != null)
            document.body.removeChild(document.getElementById("svg3"));
        if(document.getElementById("svg4") != null)
            document.body.removeChild(document.getElementById("svg4"));
        if(document.getElementById("insertImages") != null)
        document.getElementById("insertImages").style.display="none";
        if(document.getElementById("china_rank") != null)
        document.getElementById("china_rank").style.display="none";
    }
}

function staticimages(i){
    if(document.getElementById("svg1") != null)
        document.body.removeChild(document.getElementById("svg1"));
    if(document.getElementById("svg1.1")!= null)
        document.body.removeChild(document.getElementById("svg1.1"));
    if(document.getElementById("svg2") != null)
        document.body.removeChild(document.getElementById("svg2"));
    if(document.getElementById("svg3") != null)
        document.body.removeChild(document.getElementById("svg3"));
    if(document.getElementById("svg4") != null)
        document.body.removeChild(document.getElementById("svg4"));
    if(document.getElementById("myCarousel") != null)
        document.getElementById("myCarousel").style.display="none";
    if(document.getElementById("insertImages") != null)
        document.getElementById("insertImages").style.display="block";
    if(document.getElementById("china_rank") != null)
        document.getElementById("china_rank").style.display="none";
    if(i == 1){
        document.getElementById("insertImages").src="/static/bootstrap/images/nation_count.png";
        // document.getElementById("imagesDiv").innerHTML='<img src="../images/nation_count.png" height="800" width="1000" />';
    }
}
function show_ranks(i){
    if(document.getElementById("svg1") != null)
        document.body.removeChild(document.getElementById("svg1"));
    if(document.getElementById("svg1.1") != null)
        document.body.removeChild(document.getElementById("svg1.1"));
    if(document.getElementById("svg2") != null)
        document.body.removeChild(document.getElementById("svg2"));
    if(document.getElementById("svg3") != null)
        document.body.removeChild(document.getElementById("svg3"));
    if(document.getElementById("svg4") != null)
        document.body.removeChild(document.getElementById("svg4"));
    if(document.getElementById("myCarousel") != null)
        document.getElementById("myCarousel").style.display="none";
    if(document.getElementById("insertImages") != null)
        document.getElementById("insertImages").style.display="none";
    if(document.getElementById("china_rank") != null)
        document.getElementById("china_rank").style.display="none";//要是不需要重新加载需要删除这条
    var isrepeat1=false;
    var isrepeat2=false;
    if(i==1) {
        document.getElementById("china_rank").style.display = "block";
        show_china();
        //isrepeat1 = true;
        //isrepeat2=false;
    }
    //}else{
    //    document.getElementById("china_rank").style.display="block";
    //}
    if(i==2) {
        document.getElementById("china_rank").style.display = "block";
        show_C();
        //isrepeat2 = true;
        //isrepeat1=false;
    }
    //}else{
    //    document.getElementById("china_rank").style.display="block";
    //}
}

function searchUser(){
    var username = document.getElementById("searchUsername").value;
    //document.getElementById("userinfo").style.display="block";
    //$('#userinfo').github_user_widget(username);
    document.getElementById("userinfo").setAttribute("data-user",username);
}
