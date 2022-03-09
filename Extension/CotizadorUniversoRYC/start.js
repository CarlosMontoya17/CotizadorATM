window.onload = function() {
    if(document.getElementById("nss")){
      var value = document.getElementById("nss").value;
      if(value.length == 0){
        var url = new URL(window.location.href);
        if(url.searchParams.get("nss")!=null){
          var nss = url.searchParams.get("nss");
          var date = url.searchParams.get("date");
          var name = url.searchParams.get("name");
          var id = url.searchParams.get("id");
          localStorage.setItem("nss", nss);
          localStorage.setItem("date", date);
          localStorage.setItem("name", name);
          localStorage.setItem("id", id);
        }else{
          var nss = localStorage.getItem("nss");
          var date = localStorage.getItem("date");
          var name = localStorage.getItem("name");
          var id = localStorage.getItem("id");
        }
        document.getElementById("nss").value = nss;
        document.getElementsByName("day")[0].value = 1;
        document.getElementsByName("month")[0].value = 10;
        document.getElementsByName("year")[0].value = 1961;
        document.getElementsByName("code")[0].value = 11111;
        var div1 = document.getElementById("form");
        div1.getElementsByTagName("a")[1].click();
      }else if(document.getElementById("result:financiero")){
        table = document.getElementById("result:financiero");
        tr = table.getElementsByTagName("tr")[1];
        td = tr.getElementsByTagName("td")[2];
        tr2 = table.getElementsByTagName("tr")[2];
        td2 = tr2.getElementsByTagName("td")[2];
        linea4= td2.innerHTML;
        tr3 = table.getElementsByTagName("tr")[3];
        td3 = tr3.getElementsByTagName("td")[2];
        tr4 = table.getElementsByTagName("tr")[4];
        td4 = tr4.getElementsByTagName("td")[2];
        linea2= td4.innerHTML;
        span = document.getElementById("result:descuentoMensualAux");
        descuento= span.innerHTML;
        linea4 = parseFloat(linea4.replace(/,/, ''));
        linea2 = parseFloat(linea2.replace(/,/, ''));
        descuento = parseFloat(descuento.replace(/,/, ''));
        var aplica;
        if(linea4 >= 100000){
          aplica = "si";
        }else{
          aplica = "no";
        }
        var http = new XMLHttpRequest();
        var url = 'https://gruporyc.com.mx:8080/api/mainvr/upData/';
        var params = "superId="+localStorage.getItem("id")+"&nombre="+localStorage.getItem("name")+"&nss="+localStorage.getItem("nss")+"&fechaNacimiento="+localStorage.getItem("date")+"&montolinea4="+linea4+"&montolinea2="+linea2+"&descMensual="+descuento+"&aplica="+aplica+"&excepcion=null";
        http.open('POST', url, true);
        http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        http.send(params);
      }
    }else{
      if(document.URL == 'https://www.mi-portal-infonavit.com/checar-puntos'){
        mensaje = document.getElementsByTagName("div")[14];
        error = mensaje.innerHTML.trim();
        console.log(error)
        var http = new XMLHttpRequest();
        var url = 'https://gruporyc.com.mx:8080/api/mainvr/upData/';
        var params = "superId="+localStorage.getItem("id")+"&nombre="+localStorage.getItem("name")+"&nss="+localStorage.getItem("nss")+"&fechaNacimiento="+localStorage.getItem("date")+"&excepcion="+error+"&aplica=no";
        http.open('POST', url, true);
        http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        http.send(params);
      }
      
    }
    /*if(document.getElementById("precalif:nssTitular") && document.getElementById("precalif:dialog").getAttribute("aria-hidden")=="true"){
    document.getElementsByTagName("span")[1].click();
    document.getElementById("precalif:console0_1").click();
    var url = new URL(window.location.href);
    if(url.searchParams.get("nss")!=null){
      var nss = url.searchParams.get("nss");
      var date = url.searchParams.get("date");
      var name = url.searchParams.get("name");
      var id = url.searchParams.get("id");
      localStorage.setItem("nss", nss);
      localStorage.setItem("date", date);
      localStorage.setItem("name", name);
      localStorage.setItem("id", id);
    }else{
      var nss = localStorage.getItem("nss");
      var date = localStorage.getItem("date");
      var name = localStorage.getItem("name");
      var id = localStorage.getItem("id");
    }
    document.getElementById("precalif:nssTitular").value = nss;
    document.getElementById("precalif:fechaTitular").value = date;
    setTimeout(function(){ document.getElementById("precalif:j_id1653908522_1_4545a122").click(); }, 11000);
  }else if(document.getElementById("precalif:dialog").getAttribute("aria-hidden")=="false"){
    table = document.getElementById("precalif:j_id1653908522_1_4545a0c0");
    tr = table.getElementsByTagName("tr")[2];
    td = tr.getElementsByTagName("td")[0];
    span = tr.getElementsByTagName("span")[0];
    excepcion = span.innerHTML;
    var http = new XMLHttpRequest();
    var url = 'https://gruporyc.com.mx:8080/api/prospectosnl/add/';
    var params = "superId="+localStorage.getItem("id")+"&nombre="+localStorage.getItem("name")+"&nss="+localStorage.getItem("nss")+"&fechaNacimiento="+localStorage.getItem("date")+"&excepcion="+excepcion;
    http.open('POST', url, true);
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    http.send(params);
    setTimeout(function(){ socket.emit('close', ''); }, 1500);
  }else if(document.getElementById("result:autoriza_r")){
    document.getElementsByTagName("span")[2].click();
    document.getElementById("result:j_id1386474166_1_3c48b787").click();
  }else if(document.getElementById("result:financiero")){
    table = document.getElementsByTagName("table")[4];
    tr = table.getElementsByTagName("tr")[3];
    td = tr.getElementsByTagName("td")[2];
    linea4= td.innerHTML;

    tr2 = table.getElementsByTagName("tr")[5];
    td2 = tr2.getElementsByTagName("td")[2];
    linea2= td2.innerHTML;

    tr3 = table.getElementsByTagName("tr")[4];
    td3 = tr3.getElementsByTagName("td")[2];
    descMensual = td3.innerHTML;
    linea4 = parseFloat(linea4.replace(/,/, ''));
    linea2 = parseFloat(linea2.replace(/,/, ''));
    descMensual = parseFloat(descMensual.replace(/,/, ''));

    if(linea4 >= 97000){
      let aplica = "si";
    }else{
      let aplica = "no";
    }
    var http = new XMLHttpRequest();
    var url = 'https://gruporyc.com.mx:8080/api/prospectosnl/add/';
    var params = "superId="+localStorage.getItem("id")+"&nombre="+localStorage.getItem("name")+"&nss="+localStorage.getItem("nss")+"&fechaNacimiento="+localStorage.getItem("date")+"&montolinea4="+linea4+"&montolinea2="+linea2+"&descMensual="+descMensual+"&aplica="+aplica+"&excepcion="+excepcion;
    http.open('POST', url, true);
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    http.send(params);
  }*/
};