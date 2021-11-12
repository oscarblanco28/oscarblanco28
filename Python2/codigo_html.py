### Proyecto de automatización valores del NAS.

## Este es el codigo de entrada para el NAS
html_doc="""
<div id="header">
		<h1 id="logo"><img src="http://nas.net-uno.net//nas2/htdocs/img/logo.png"></h1>
		<form name="entrada" id="entrada" method="post" class="searchform" action="redirect.php">
			<table>
			<tbody><tr>
				<td>Usuario:</td>
				<td><input type="text" name="login" class="textbox"></td> #AQUI PIDE USUARIO PARA ENTRAR
			</tr>
			<tr>
				<td>Contraseña:</td>
				<td><input type="password" name="password" class="textbox" onkeypress="checkKey(event);"></td> #contraseña aqui
			</tr>
			<tr align="right">
				<td><a href="javascript:document.entrada.submit();">Entrar</a></td> #BOTON DE ENTRADA
				<td><a href="general_recordar_passwd.php">Recordar Contraseña</a></td>
			</tr>
			<tr>
				<td colspan="2"><b style="color:red;"></b></td>
			</tr>_
			</tbody></table>
</form>
	</div>

	## AQUI TERMINA ELCODIGO DE ENTRADA

## AQUI COMIENZA EL MENU DE AL LADO

<div id="content-wrap">
			<div id="sidebar">
			<ul id="theMenu"><li>
				<a class="unhead" href="http://nas.net-uno.net//nas2/htdocs//index.php">Inicio</a>
			</li>
				<li><a href="#" class="head">DUMS3 Maracaibo</a>
					<ul style="display: none;">
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_nodos.php">Consultar Nodos</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_cmts.php">Consultar CMTS</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_optdhcp.php">Consultar Opciones DHCP</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_nets.php">Consultar Redes</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_emta.php">Consultar EMTA</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_cm.php">Consultar CM</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_productos.php">Consultar Productos</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_jobs.php">Consultar Jobs Pendientes</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_jobslogs.php">Consultar JobsLogs</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_logs_sys.php">Consultar Logs SYS</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_rep_cm.php">Reporte CM</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_logs_dhcp.php">Consultar Logs DHCP</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/dums3_mbo/dums_con_logs_tftp.php">Consultar Logs TFTP</a></li>
					</ul>
					</li>
				<li><a href="#" class="head">Ftth Maracaibo</a>
					<ul style="display: none;">
					<li><a href="http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_con_ont.php">Consultar ONT</a></li> ## Esto es lo que nos interesa!!!
					<li><a href="http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_con_nodos.php">Consultar Nodos</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_con_jobs.php">Consultar Jobs</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_con_jobslogs.php">Consultar JobsLogs</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_con_productos.php">Consultar Productos</a></li>
					<li><a href="http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_rep_ont.php">Reporte ONT</a></li>
					</ul>
					</li>
				</ul>
				</div>
	  		<div id="main">
				<a name="TemplateInfo"></a>
				<h1>Bienvenidos</h1>

				<p>A un año del lanzamiento del NAS (NetUno Application Server),
				nos complace presentarles la segunda version, con nuevas caracteristicas y
				mas utilidades.</p>

				<h1>Nuevos Formatos</h1>

				<p>Ya estan disponibles para descarga los nuevos formatos:</p>
				<ul>
					<li><a href="../Procedimientos/NAC-ING-FOR-ALL-ALL-413_R1_0.doc">Formato para solicitud de soporte.</a></li>
				</ul>


	  		</div>
			<br>

	<!-- content-wrap ends here -->
	</div>

	## Una vez que se llega a http://nas.net-uno.net//nas2/htdocs/ftth_mbo/ftth_con_ont.php seleccionando un nodo y dandole a buscar

<div id="main">
<script language="JavaScript">

function ajax_handler(enlace,func,id,args){
	switch (func){
		case 'BUSCAR':
			var codigo = args.split(",");
		 	text_codigo = 'nuevo';
		 	text_abonado = document.getElementById("text_abonado_"+text_codigo).value;
		 	text_contrato = document.getElementById("text_contrato_"+text_codigo).value;
		 	text_serial = document.getElementById("text_serial_"+text_codigo).value;
		 	text_mac = document.getElementById("text_mac_"+text_codigo).value;
		 	text_producto = document.getElementById("text_producto_"+text_codigo).value;
		 	text_nodo = document.getElementById("text_nodo_"+text_codigo).value;
		 	text_usuario = document.getElementById("text_usuario_"+text_codigo).value;
  			args = codigo[0] + "," + codigo[1] + "," + text_abonado + "," + text_contrato + "," + text_serial + "," + text_producto + "," + text_nodo + "," + text_usuario + "," + text_mac;
		break;
		case 'MOSTRAR':
			var codigo = args.split(",");
			args = codigo[0] + "," + codigo[1] + "," + codigo[2]
		break;
		case 'CORTAR':
			if(!confirm("Desea cortar el ONT "+args+"?")){
				return;
			}
		break;
		case 'MODIFICAR':
			alert('MODIFICAR');
			return;
		break;
		case 'ELIMINAR':
			if(!confirm("Desea eliminar el ONT "+args+"?")){
				return;
			}
		break;

	}
	document.getElementById("ftth_con_ont_div_1").innerHTML = '<img src="http://nas.net-uno.net//nas2/htdocs/img/loading.gif"/>';
	agent.call(enlace,'ajax_handler','_callback',func,args);
}
function _callback(str){
    try{
    	eval(str);
        document.getElementById("ftth_con_ont_div_1").innerHTML = '';
    }catch(e){
        document.getElementById("ftth_con_ont_div_1").innerHTML = str;
    }
}

var newwindow = null;

function ajax_handler_popup(enlace,func,id,args){
	newwindow = window.open("http://nas.net-uno.net//nas2/htdocs/img/loading.gif","NAS2","width=800,height=600,resizable=1,menubar=0,scrollbars=1");
	agent.call(enlace,'ajax_handler_popup','_popup',func,args);
}

function _popup(content){
	var tmp = newwindow.document;
    tmp.write(content);
    tmp.close();
}

</script>



<!-- Esto deberian ser variables para no tener q tocar el codigo HTML, titulo y div -->
<h1>Consulta de ONT - ftth_mbo</h1>
<br>
<h1>Buscar</h1>
<br>
<table width="100%" align="center">
	<tbody><tr>
		<td>Abonado</td>
		<td><input id="text_abonado_nuevo" type="text"></td> ## Aqui  se pone el numero de abonado
	</tr>
	<tr>
		<td>Contrato</td>
		<td><input id="text_contrato_nuevo" type="text"></td>
	</tr>
	<tr>
		<td>Serial</td>
		<td><input id="text_serial_nuevo" type="text"></td>
	</tr>
	<tr>
		<td>Usuario</td>
		<td><input id="text_usuario_nuevo" type="text"></td>
	</tr>
	<tr>
		<td>MAC</td>
		<td><input id="text_mac_nuevo" type="text"></td>
	</tr>
	<tr>
		<td>Producto</td>
		<td>
			<select id="text_producto_nuevo">
				<option value="">Cualquiera</option>
								<option value="cortado">cortado</option>
								<option value="Fibranet100Mb">Fibranet100Mb</option>
								<option value="Fibranet200Mb">Fibranet200Mb</option>
								<option value="Fibranet50Mb">Fibranet50Mb</option>
								<option value="FiberPonRoot50Mb">FiberPonRoot50Mb</option>
								<option value="FiberPonBusiness100Mb">FiberPonBusiness100Mb</option>
							</select>
		</td>
	</tr>
	<tr>
		<td>Nodo</td>
		<td>
			<select id="text_nodo_nuevo">
				<option value="">Cualquiera</option>
								<option value="MBOHED00100A">MBOHED00100A-MBOHED00100A</option>
								<option value="MBOHED00106A">MBOHED00106A-MBOHED00106A</option>
								<option value="MBOHED00108A">MBOHED00108A-MBOHED00108A</option>
								<option value="MBOHED00109A">MBOHED00109A-MBOHED00109A</option>
								<option value="MBOHED00101A">MBOHED00101A-MBOHED00101A</option>
								<option value="MBOHED00110A">MBOHED00110A-MBOHED00110A</option>
								<option value="MBOHED00111A">MBOHED00111A-MBOHED00111A</option>
								<option value="MBOHED00112A">MBOHED00112A-MBOHED00112A</option>
								<option value="MBOHED00113A">MBOHED00113A-MBOHED00113A</option>
								<option value="MBOHED00114A">MBOHED00114A-MBOHED00114A</option>
								<option value="MBOHED00102A">MBOHED00102A-MBOHED00102A</option>
								<option value="MBOHED00103A">MBOHED00103A-MBOHED00103A</option>
								<option value="MBOHED00104A">MBOHED00104A-MBOHED00104A</option>
								<option value="MBOHED00105A">MBOHED00105A-MBOHED00105A</option>
								<option value="MBOHED00107A">MBOHED00107A-MBOHED00107A</option>
								<option value="MBOHED00200A">MBOHED00200A-MBOHED00200A</option>
								<option value="MBOHED00202A">MBOHED00202A-MBOHED00202A</option>
								<option value="MBOHED00204A">MBOHED00204A-MBOHED00204A</option>
								<option value="MBOHED00205A">MBOHED00205A-MBOHED00205A</option>
								<option value="MBOHED00206A">MBOHED00206A-MBOHED00206A</option>
								<option value="MBOHED00207A">MBOHED00207A-MBOHED00207A</option>
								<option value="MBOHED00208A">MBOHED00208A-MBOHED00208A</option>
								<option value="MBOHED00209A">MBOHED00209A-MBOHED00209A</option>
								<option value="MBOHED00201A">MBOHED00201A-MBOHED00201A</option>
								<option value="MBOHED00211A">MBOHED00211A-MBOHED00211A</option>
								<option value="MBOHED00214A">MBOHED00214A-MBOHED00214A</option>
								<option value="MBOHED00215A">MBOHED00215A-MBOHED00215A</option>
								<option value="MBOHED00203A">MBOHED00203A-MBOHED00203A</option>
								<option value="MBODIV00000A">MBODIV00000A-MBODIV00000A</option>
								<option value="MBODIV00008A">MBODIV00008A-MBODIV00008A</option>
								<option value="MBODIV00010A">MBODIV00010A-MBODIV00010A</option>
								<option value="MBODIV00014A">MBODIV00014A-MBODIV00014A</option>
								<option value="MBODIV00100A">MBODIV00100A-MBODIV00100A</option>
								<option value="MBODIV00101A">MBODIV00101A-MBODIV00101A</option>
								<option value="MBODIV00102A">MBODIV00102A-MBODIV00102A</option>
								<option value="MBODIV00103A">MBODIV00103A-MBODIV00103A</option>
								<option value="MBODIV00107A">MBODIV00107A-MBODIV00107A</option>
								<option value="MBODIV00108A">MBODIV00108A-MBODIV00108A</option>
								<option value="MBODIV00109A">MBODIV00109A-MBODIV00109A</option>
								<option value="MBODIV00110A">MBODIV00110A-MBODIV00110A</option>
								<option value="MBODIV00111A">MBODIV00111A-MBODIV00111A</option>
								<option value="MBODIV00112A">MBODIV00112A-MBODIV00112A</option>
								<option value="MBODIV00114A">MBODIV00114A-MBODIV00114A</option>
							</select>
		</td>
	</tr>
</tbody></table>
<br>
<h2>
	<a href="javascript:ajax_handler('ajax/ftth_con_ont.php','BUSCAR','ftth_con_ont_div_1','1,1')">Buscar</a> ##Aqui se hace click en BUSCAR
</h2>
<br>
<div id="ftth_con_ont_div_1"><h1>Listado</h1>
<br>

<table width="100%" align="center">
<tbody><tr class="MainGridHeaderCell">
	<td>ID ONT</td>
	<td>ABONADO</td>
	<td>CONTRATO</td>
	<td>SERIAL</td>
	<td>MAC</td>
	<td>PRODUCTO</td>
	<td>NODO</td>
	<td>USUARIO</td>
</tr>
						<tr id="10267199" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10267199');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							41
						</label>
					</td>
					<td>
						<label>
							1009117
						</label>
					</td>
					<td>
						<label>
							10267199
						</label>
					</td>
					<td>
						<label>
							485754434D9A25A3
						</label>
					</td>
					<td>
						<label>
							9
						</label>
					</td>
					<td>
						<label>
							Fibranet200Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10267199
						</label>
					</td>
			 </tr>
						<tr id="10263047" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263047');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							4
						</label>
					</td>
					<td>
						<label>
							1014131
						</label>
					</td>
					<td>
						<label>
							10263047
						</label>
					</td>
					<td>
						<label>
							485754434D9AB4A3
						</label>
					</td>
					<td>
						<label>
							9
						</label>
					</td>
					<td>
						<label>
							Fibranet200Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263047
						</label>
					</td>
			 </tr>
						<tr id="10263050" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263050');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							2
						</label>
					</td>
					<td>
						<label>
							1030256
						</label>
					</td>
					<td>
						<label>
							10263050
						</label>
					</td>
					<td>
						<label>
							485754434E66ABA3
						</label>
					</td>
					<td>
						<label>
							60123C2801B8
						</label>
					</td>
					<td>
						<label>
							Fibranet200Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263050
						</label>
					</td>
			 </tr>
						<tr id="10263046" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263046');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							3
						</label>
					</td>
					<td>
						<label>
							944112
						</label>
					</td>
					<td>
						<label>
							10263046
						</label>
					</td>
					<td>
						<label>
							HWTC046A3F9E
						</label>
					</td>
					<td>
						<label>
							20283EEE4599
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263046
						</label>
					</td>
			 </tr>
						<tr id="10263100" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263100');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							7
						</label>
					</td>
					<td>
						<label>
							1030302
						</label>
					</td>
					<td>
						<label>
							10263100
						</label>
					</td>
					<td>
						<label>
							HWTC046C969E
						</label>
					</td>
					<td>
						<label>
							20283EEE67BC
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263100
						</label>
					</td>
			 </tr>
						<tr id="10263051" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263051');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							5
						</label>
					</td>
					<td>
						<label>
							1018189
						</label>
					</td>
					<td>
						<label>
							10263051
						</label>
					</td>
					<td>
						<label>
							HWTC053E2D9E
						</label>
					</td>
					<td>
						<label>
							20283EF9101D
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263051
						</label>
					</td>
			 </tr>
						<tr id="10263077" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263077');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							1
						</label>
					</td>
					<td>
						<label>
							526963
						</label>
					</td>
					<td>
						<label>
							10263077
						</label>
					</td>
					<td>
						<label>
							HWTC053FA19E
						</label>
					</td>
					<td>
						<label>
							20283EF92301
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							HWTC053FA19E
						</label>
					</td>
			 </tr>
						<tr id="10263240" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263240');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							12
						</label>
					</td>
					<td>
						<label>
							612014
						</label>
					</td>
					<td>
						<label>
							10263240
						</label>
					</td>
					<td>
						<label>
							HWTC0541F89E
						</label>
					</td>
					<td>
						<label>
							20283EF9416C
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263240
						</label>
					</td>
			 </tr>
						<tr id="10266170" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10266170');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							37
						</label>
					</td>
					<td>
						<label>
							490578
						</label>
					</td>
					<td>
						<label>
							10266170
						</label>
					</td>
					<td>
						<label>
							HWTC2602B69E
						</label>
					</td>
					<td>
						<label>
							9835ED03737E
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10266170
						</label>
					</td>
			 </tr>
						<tr id="10266195" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10266195');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							39
						</label>
					</td>
					<td>
						<label>
							1034326
						</label>
					</td>
					<td>
						<label>
							10266195
						</label>
					</td>
					<td>
						<label>
							HWTC2608619E
						</label>
					</td>
					<td>
						<label>
							9835ED03BD2D
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10266195
						</label>
					</td>
			 </tr>
						<tr id="10266149" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10266149');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							43
						</label>
					</td>
					<td>
						<label>
							1034223
						</label>
					</td>
					<td>
						<label>
							10266149
						</label>
					</td>
					<td>
						<label>
							HWTC278D209E
						</label>
					</td>
					<td>
						<label>
							9835ED1A329D
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10266149
						</label>
					</td>
			 </tr>
						<tr id="10266925" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10266925');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							38
						</label>
					</td>
					<td>
						<label>
							625494
						</label>
					</td>
					<td>
						<label>
							10266925
						</label>
					</td>
					<td>
						<label>
							HWTC278D639E
						</label>
					</td>
					<td>
						<label>
							9835ED1A3604
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10266925
						</label>
					</td>
			 </tr>
						<tr id="10266497" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10266497');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							42
						</label>
					</td>
					<td>
						<label>
							605259
						</label>
					</td>
					<td>
						<label>
							10266497
						</label>
					</td>
					<td>
						<label>
							HWTC27A5429E
						</label>
					</td>
					<td>
						<label>
							9835ED1B6C57
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10266497
						</label>
					</td>
			 </tr>
						<tr id="10265772" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265772');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							30
						</label>
					</td>
					<td>
						<label>
							1033578
						</label>
					</td>
					<td>
						<label>
							10265772
						</label>
					</td>
					<td>
						<label>
							HWTC2EBA6B9D
						</label>
					</td>
					<td>
						<label>
							D0EFC11EAD20
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265772
						</label>
					</td>
			 </tr>
						<tr id="10263165" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263165');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							10
						</label>
					</td>
					<td>
						<label>
							581838
						</label>
					</td>
					<td>
						<label>
							10263165
						</label>
					</td>
					<td>
						<label>
							HWTC2EBD2F9D
						</label>
					</td>
					<td>
						<label>
							D0EFC11ED114
						</label>
					</td>
					<td>
						<label>
							Fibranet100Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263165
						</label>
					</td>
			 </tr>
						<tr id="10263098" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263098');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							8
						</label>
					</td>
					<td>
						<label>
							1030307
						</label>
					</td>
					<td>
						<label>
							10263098
						</label>
					</td>
					<td>
						<label>
							HWTC2EBD349D
						</label>
					</td>
					<td>
						<label>
							D0EFC11ED155
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263098
						</label>
					</td>
			 </tr>
						<tr id="10265675" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265675');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							29
						</label>
					</td>
					<td>
						<label>
							1033265
						</label>
					</td>
					<td>
						<label>
							10265675
						</label>
					</td>
					<td>
						<label>
							HWTC2EBD529D
						</label>
					</td>
					<td>
						<label>
							D0EFC11ED2DB
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265675
						</label>
					</td>
			 </tr>
						<tr id="10263078" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263078');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							6
						</label>
					</td>
					<td>
						<label>
							877984
						</label>
					</td>
					<td>
						<label>
							10263078
						</label>
					</td>
					<td>
						<label>
							HWTC2EBD549D
						</label>
					</td>
					<td>
						<label>
							D0EFC11ED2F5
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263078
						</label>
					</td>
			 </tr>
						<tr id="10265634" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265634');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							28
						</label>
					</td>
					<td>
						<label>
							1033342
						</label>
					</td>
					<td>
						<label>
							10265634
						</label>
					</td>
					<td>
						<label>
							HWTC2ED30D9D
						</label>
					</td>
					<td>
						<label>
							D0EFC11FED5A
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265634
						</label>
					</td>
			 </tr>
						<tr id="10264573" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10264573');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							17
						</label>
					</td>
					<td>
						<label>
							1031788
						</label>
					</td>
					<td>
						<label>
							10264573
						</label>
					</td>
					<td>
						<label>
							HWTC2F9DF89D
						</label>
					</td>
					<td>
						<label>
							HWTC2F9DF89D
						</label>
					</td>
					<td>
						<label>
							Fibranet100Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10264573
						</label>
					</td>
			 </tr>
						<tr id="10264718" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10264718');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							19
						</label>
					</td>
					<td>
						<label>
							1031949
						</label>
					</td>
					<td>
						<label>
							10264718
						</label>
					</td>
					<td>
						<label>
							HWTC2F9E199D
						</label>
					</td>
					<td>
						<label>
							D0EFC12A42D2
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10264718
						</label>
					</td>
			 </tr>
						<tr id="10264670" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10264670');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							22
						</label>
					</td>
					<td>
						<label>
							1031832
						</label>
					</td>
					<td>
						<label>
							10264670
						</label>
					</td>
					<td>
						<label>
							HWTC2F9E2B9D
						</label>
					</td>
					<td>
						<label>
							D0EFC12A43BC
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10264670
						</label>
					</td>
			 </tr>
						<tr id="10274139" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10274139');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							48
						</label>
					</td>
					<td>
						<label>
							503437
						</label>
					</td>
					<td>
						<label>
							10274139
						</label>
					</td>
					<td>
						<label>
							HWTC3CD76DA3
						</label>
					</td>
					<td>
						<label>
							A0DF15CD7F60
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							HWTC3CD76DA3
						</label>
					</td>
			 </tr>
						<tr id="10274152" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10274152');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							18
						</label>
					</td>
					<td>
						<label>
							1010655
						</label>
					</td>
					<td>
						<label>
							10274152
						</label>
					</td>
					<td>
						<label>
							HWTC3CD97BA3
						</label>
					</td>
					<td>
						<label>
							A0DF15CDA24E
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							HWTC3CD97BA3
						</label>
					</td>
			 </tr>
						<tr id="10264364" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10264364');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							15
						</label>
					</td>
					<td>
						<label>
							1031545
						</label>
					</td>
					<td>
						<label>
							10264364
						</label>
					</td>
					<td>
						<label>
							HWTC40E3599D
						</label>
					</td>
					<td>
						<label>
							HWTC40E3599D
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10264364
						</label>
					</td>
			 </tr>
						<tr id="10264564" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10264564');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							16
						</label>
					</td>
					<td>
						<label>
							1031512
						</label>
					</td>
					<td>
						<label>
							10264564
						</label>
					</td>
					<td>
						<label>
							HWTC40E3789D
						</label>
					</td>
					<td>
						<label>
							HWTC40E3789D
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10264564
						</label>
					</td>
			 </tr>
						<tr id="10265799" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265799');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							31
						</label>
					</td>
					<td>
						<label>
							507525
						</label>
					</td>
					<td>
						<label>
							10265799
						</label>
					</td>
					<td>
						<label>
							HWTC454EB39D
						</label>
					</td>
					<td>
						<label>
							40EEDD81D044
						</label>
					</td>
					<td>
						<label>
							Fibranet100Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265799
						</label>
					</td>
			 </tr>
						<tr id="10265945" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265945');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							35
						</label>
					</td>
					<td>
						<label>
							1033831
						</label>
					</td>
					<td>
						<label>
							10265945
						</label>
					</td>
					<td>
						<label>
							HWTC454F449D
						</label>
					</td>
					<td>
						<label>
							40EEDD81D7A1
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265945
						</label>
					</td>
			 </tr>
						<tr id="10268368" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10268368');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							47
						</label>
					</td>
					<td>
						<label>
							616979
						</label>
					</td>
					<td>
						<label>
							10268368
						</label>
					</td>
					<td>
						<label>
							HWTC454F4A9D
						</label>
					</td>
					<td>
						<label>
							40EEDD81D7EF
						</label>
					</td>
					<td>
						<label>
							Fibranet100Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10268368
						</label>
					</td>
			 </tr>
						<tr id="10265915" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265915');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							33
						</label>
					</td>
					<td>
						<label>
							1033750
						</label>
					</td>
					<td>
						<label>
							10265915
						</label>
					</td>
					<td>
						<label>
							HWTC454F5F9D
						</label>
					</td>
					<td>
						<label>
							40EEDD81D900
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265915
						</label>
					</td>
			 </tr>
						<tr id="10268235" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10268235');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							46
						</label>
					</td>
					<td>
						<label>
							625452
						</label>
					</td>
					<td>
						<label>
							10268235
						</label>
					</td>
					<td>
						<label>
							HWTC454F7E9D
						</label>
					</td>
					<td>
						<label>
							40EEDD81DA93
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10268235
						</label>
					</td>
			 </tr>
						<tr id="10268190" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10268190');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							45
						</label>
					</td>
					<td>
						<label>
							1018362
						</label>
					</td>
					<td>
						<label>
							10268190
						</label>
					</td>
					<td>
						<label>
							HWTC454F939D
						</label>
					</td>
					<td>
						<label>
							40EEDD81DBA4
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10268190
						</label>
					</td>
			 </tr>
						<tr id="10274856" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10274856');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							49
						</label>
					</td>
					<td>
						<label>
							1043644
						</label>
					</td>
					<td>
						<label>
							10274856
						</label>
					</td>
					<td>
						<label>
							HWTC4E6B48A3
						</label>
					</td>
					<td>
						<label>
							60123C285025
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							HWTC4E6B48A3
						</label>
					</td>
			 </tr>
						<tr id="10263174" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263174');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							11
						</label>
					</td>
					<td>
						<label>
							519187
						</label>
					</td>
					<td>
						<label>
							10263174
						</label>
					</td>
					<td>
						<label>
							HWTC7B89629E
						</label>
					</td>
					<td>
						<label>
							FCBCD1C843A1
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263174
						</label>
					</td>
			 </tr>
						<tr id="10263433" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263433');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							13
						</label>
					</td>
					<td>
						<label>
							1030470
						</label>
					</td>
					<td>
						<label>
							10263433
						</label>
					</td>
					<td>
						<label>
							HWTC7B8A159E
						</label>
					</td>
					<td>
						<label>
							FCBCD1C84CB8
						</label>
					</td>
					<td>
						<label>
							Fibranet100Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263433
						</label>
					</td>
			 </tr>
						<tr id="10263425" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10263425');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							14
						</label>
					</td>
					<td>
						<label>
							613491
						</label>
					</td>
					<td>
						<label>
							10263425
						</label>
					</td>
					<td>
						<label>
							HWTC7B8A3F9E
						</label>
					</td>
					<td>
						<label>
							FCBCD1C84EDA
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10263425
						</label>
					</td>
			 </tr>
						<tr id="10266083" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10266083');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							32
						</label>
					</td>
					<td>
						<label>
							605951
						</label>
					</td>
					<td>
						<label>
							10266083
						</label>
					</td>
					<td>
						<label>
							HWTC86FD9E9E
						</label>
					</td>
					<td>
						<label>
							F41D6B784517
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10266083
						</label>
					</td>
			 </tr>
						<tr id="10265390" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265390');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							26
						</label>
					</td>
					<td>
						<label>
							537398
						</label>
					</td>
					<td>
						<label>
							10265390
						</label>
					</td>
					<td>
						<label>
							HWTC87680B9D
						</label>
					</td>
					<td>
						<label>
							4857024B0416
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265390
						</label>
					</td>
			 </tr>
						<tr id="10265386" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265386');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							24
						</label>
					</td>
					<td>
						<label>
							575835
						</label>
					</td>
					<td>
						<label>
							10265386
						</label>
					</td>
					<td>
						<label>
							HWTC876A749D
						</label>
					</td>
					<td>
						<label>
							4857024B236B
						</label>
					</td>
					<td>
						<label>
							Fibranet100Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265386
						</label>
					</td>
			 </tr>
						<tr id="10265394" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265394');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							25
						</label>
					</td>
					<td>
						<label>
							1033048
						</label>
					</td>
					<td>
						<label>
							10265394
						</label>
					</td>
					<td>
						<label>
							HWTC876ACA9D
						</label>
					</td>
					<td>
						<label>
							HWTC876ACA9D
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265394
						</label>
					</td>
			 </tr>
						<tr id="10266505" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10266505');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							44
						</label>
					</td>
					<td>
						<label>
							1034446
						</label>
					</td>
					<td>
						<label>
							10266505
						</label>
					</td>
					<td>
						<label>
							HWTCBB06569D
						</label>
					</td>
					<td>
						<label>
							485702D04DC4
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10266505
						</label>
					</td>
			 </tr>
						<tr id="10266121" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10266121');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							40
						</label>
					</td>
					<td>
						<label>
							616847
						</label>
					</td>
					<td>
						<label>
							10266121
						</label>
					</td>
					<td>
						<label>
							HWTCBB1F229D
						</label>
					</td>
					<td>
						<label>
							485702D19020
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10266121
						</label>
					</td>
			 </tr>
						<tr id="10265333" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265333');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							21
						</label>
					</td>
					<td>
						<label>
							1033016
						</label>
					</td>
					<td>
						<label>
							10265333
						</label>
					</td>
					<td>
						<label>
							HWTCBB20C09D
						</label>
					</td>
					<td>
						<label>
							485702D1A526
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265333
						</label>
					</td>
			 </tr>
						<tr id="10264951" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10264951');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							20
						</label>
					</td>
					<td>
						<label>
							602558
						</label>
					</td>
					<td>
						<label>
							10264951
						</label>
					</td>
					<td>
						<label>
							HWTCBB21909D
						</label>
					</td>
					<td>
						<label>
							485702D1AFB6
						</label>
					</td>
					<td>
						<label>
							Fibranet100Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10264951
						</label>
					</td>
			 </tr>
						<tr id="10265332" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265332');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							23
						</label>
					</td>
					<td>
						<label>
							624590
						</label>
					</td>
					<td>
						<label>
							10265332
						</label>
					</td>
					<td>
						<label>
							HWTCBB23879D
						</label>
					</td>
					<td>
						<label>
							HWTCBB23879D
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265332
						</label>
					</td>
			 </tr>
						<tr id="10266910" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10266910');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							34
						</label>
					</td>
					<td>
						<label>
							1032778
						</label>
					</td>
					<td>
						<label>
							10266910
						</label>
					</td>
					<td>
						<label>
							HWTCBB258F9D
						</label>
					</td>
					<td>
						<label>
							485702D1E3A9
						</label>
					</td>
					<td>
						<label>
							Fibranet100Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10266910
						</label>
					</td>
			 </tr>
						<tr id="10265389" class="MainGridItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10265389');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							27
						</label>
					</td>
					<td>
						<label>
							559995
						</label>
					</td>
					<td>
						<label>
							10265389
						</label>
					</td>
					<td>
						<label>
							HWTCBB27A09D
						</label>
					</td>
					<td>
						<label>
							485702D1FE86
						</label>
					</td>
					<td>
						<label>
							Fibranet50Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							10265389
						</label>
					</td>
			 </tr>
						<tr id="10273708" class="MainGridAlternatingItemCell" onmouseover="changeClass('','MainGridSelectedItemCell')" onmouseout="changeClass('','MainGridAlternatingItemCell')" onclick="ajax_handler('ajax/ftth_con_ont.php','MOSTRAR','ftth_con_ont_div_1','1,1,10273708');" style="cursor: pointer; cursor: hand;">
					<td>
						<label>
							36
						</label>
					</td>
					<td>
						<label>
							895141
						</label>
					</td>
					<td>
						<label>
							10273708
						</label>
					</td>
					<td>
						<label>
							HWTCEC0DA09F
						</label>
					</td>
					<td>
						<label>
							04885F59B667
						</label>
					</td>
					<td>
						<label>
							Fibranet100Mb
						</label>
					</td>
					<td>
						<label>
							MBOHED00100A
						</label>
					</td>
					<td>
						<label>
							HWTCEC0DA09F
						</label>
					</td>
			 </tr>
			</tbody></table>
<p><b></b></p>
<br>
<br>
</div>

</div>
"""
## AQUI PUEDO SACAR LAS LISTA DE ABONADOS POR NODOS

## AQUI PUEDO AGARRAR LA MISMA PAGINA DE ARRIBA Y SOLO COPIAR LOS ABONADOS Y CAPTURAR LA INFO QUE QUIERO
html_doc2="""<pre>
display ont
 optical-info
 3 27

  -----------------------------------------------------------------------------
  ONU NNI port ID                        : 0
  Module type                            : GPON
  Module sub-type                        : CLASS B+
  Used type                              : ONU
  Encapsulation Type                     : BOSA ON BOARD
  Optical power precision(dBm)           : 3.0
  Vendor name                            : HUAWEI          
  Vendor rev                             : -
  Vendor PN                              : HW-BOB-0008     
  Vendor SN                              : 2013R0026622D   
  Date Code                              : 20-06-27
  Rx optical power(dBm)                  : -28.54
  Rx power current warning threshold(dBm): [-,-]
  Rx power current alarm threshold(dBm)  : [-29.0,-7.0]
  Tx optical power(dBm)                  : 1.98
  Tx power current warning threshold(dBm): [-,-]
  Tx power current alarm threshold(dBm)  : [0.0,5.0]
  Laser bias current(mA)                 : 6
  Tx bias current warning threshold(mA)  : [-,-]
  Tx bias current alarm threshold(mA)    : [2.000,100.000]
  Temperature(C)                         : 44
  Temperature warning threshold(C)       : [-,-]
                                       Temperature alarm threshold(C)         : [-61,95]
  Voltage(V)                             : 3.300
  Supply voltage warning threshold(V)    : [-,-]
  Supply voltage alarm threshold(V)      : [3.000,3.600]
  OLT Rx ONT optical power(dBm)          : -29.59
  CATV Rx optical power(dBm)             : -
  CATV Rx power alarm threshold(dBm)     : [-,-]
  -----------------------------------------------------------------------------
</pre>"""