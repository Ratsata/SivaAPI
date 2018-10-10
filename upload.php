<!--
Archivo:         upload.php
Programa:        SivaAPI
Proyecto:        Siva
Autor:           Sebastian Vega

===========================================
Fecha      |  Programador        | Detalles
===========================================
10-09-18      Sebastian Vega       Creacion
-->

<?php
    header('Access-Control-Allow-Origin: *');
    $action = $_REQUEST['action'];
    if(isset($_REQUEST['tipo'])) $tipo = $_REQUEST['tipo'];
	if(isset($_REQUEST['id'])) $id = $_REQUEST['id'];
	if(isset($_REQUEST['ip'])) $ip = $_REQUEST['ip'];
	if(isset($_REQUEST['uri'])) $uri = $_REQUEST['uri'];

    if ($action == 'alarm') alarm($tipo);
    if ($action == 'voice') voice();
    if ($action == 'stop') stop();
    if ($action == 'getpid') getPID('vlc');
    if ($action == 'get') echo get();
    if ($action == 'add') add($id);
    if ($action == 'remove') remove($id);
?>
<?php
    function alarm($tipo){
	if(killeable('releStart.py')>1){
		echo "FAIL";
	}else{
		echo "OK";
		exec('/usr/bin/nohup sudo python assets/releStart.py >/dev/null 2>&1 &');
		exec('/usr/bin/nohup python assets/playSound.py -t '.$tipo.' >/dev/null 2>&1 &');
	}
    }
?>
<?php
    function voice(){
	$target_path = "assets/sounds/temp";
	$target_path = $target_path ."/".basename( $_FILES['file']['name']);
	if(file_exists($target_path)) {
		chmod($target_path,0755);
		unlink($target_path);
	}
    	if (move_uploaded_file($_FILES['file']['tmp_name'], $target_path)) {
		echo "OK";
		exec('python assets/playSound.py --f '.$target_path,$output);
    	} else {
		echo "NOK";
    		echo $target_path;
    	}
    }
?>
<?php
    function stop(){
	echo "STOP";
	exec('pkill vlc');
	//exec('/usr/bin/nohup sudo python assets/releStop.py >/dev/null 2>&1 &');
	exec('sudo python assets/releStop.py');
    }
?>
<?php
    function getPID($name){
	$data = exec('pidof '.$name);
	if ($data){
		echo $data;
	}
   }
?>
<?php
    function killeable($name){
        $data = exec('pkill -fc releStart.py');
        if ($data){
            return $data;
        }else{
            return false;
        }
    }
?>
<?php
    function get(){
        $file = readJson('assets/topics.json');
        return json_encode($file);
    }
?>
<?php
    function add($serial){
        $file = readJson('assets/topics.json');
        $id = 0;
        foreach ($file as $key) {
            $id = ($key['id'] > $id ? $key['id'] : $id);
        }
        $data = array(
            'id' => $id+1,
            'nombre' => $serial
        );

        array_push($file, $data);
        if(writeJson('assets/topics.json',$file)){
            echo json_encode($file);
        }else{
            echo "NOK";
        }
   }
?>
<?php
    function remove($serial){
        $config = readJson('assets/topics.json');
        foreach ($config as $key=>$value) {
            if ($value['nombre'] === $serial){
                unset($config[$key]);
                break;
            }
        }

        if(writeJson('assets/topics.json',$config)){
            echo json_encode($config);
        }else{
            echo "NOK";
        }
    }
?>
<?php
    function readJson($file,$assoc=true){
        $data = file_get_contents($file);
        return json_decode($data,$assoc);
    }
?>
<?php
    function writeJson($file,$data){
        $fp = fopen($file, 'w');
            fwrite($fp, json_encode($data));
        fclose($fp);
        return true;
    }
?>
