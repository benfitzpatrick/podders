<?php
# debuging function
function printdebug($message){
    if(!empty($_GET['debug']))
    {
        echo "<p style='background:red; color:yellow; font-weight:bold;'>$message</p>" ;
    }
}

# connect to data base
$username="pod";
$password="podpod";
$database="pod";
mysql_connect('localhost',$username,$password);
@mysql_select_db($database) or die( "Unable to select database");

# get the web cam image
$date = date_create();
$filepath =  dirname(__FILE__) . '/images/' . date_timestamp_get($date) . '.png';
$cmd = "python " . dirname(__FILE__) . '/' . 'snapWebCam.py ' . $filepath;
popen($cmd, "r");
printdebug("web cam snap at $filepath");
printdebug( "called $cmd");
#$filepath = 'C:/Users/Theo/IntellijWorkspace/podders/resource_viewer_site/images/1354443627.png';


# run the command to annalyse the image
if(!empty($_GET['choice'])){
    $webcamresult =  trim($_GET['choice']);
}  else {
    $pythoncmd = "python " . dirname(__FILE__) . "/getchosices.py $filepath"     ;
    $handle = popen($pythoncmd, "r");
    $webcamresult =  fread($handle, 2096);
    printdebug( "Called $pythoncmd and got $webcamresult")     ;
}

#parse the result
$webcamresultbits = explode(',',$webcamresult);
$artRank = (float) $webcamresultbits[0];
$sciRank = (float) $webcamresultbits[1];
$citRank = (float) $webcamresultbits[2];
$wheelCol =  $webcamresultbits[3];

# get the most popular industry
switch (trim($wheelCol)) {
    case "green":
            $industry = "IT and Design";
            break;
    case "pink":
        $industry = "Random";
        break;
    case "blue":
        $industry = "Education, Health and Social Care";
        break;
    default:
        $industry = "Retail and Manufacturing";
        break;
}

# get the most popular  discipline
$disapline = "Art" ;
if($sciRank > $artRank )
{
    if( $sciRank > $citRank)
    {
      $disapline = 'Science'    ;
    }
    else
    {
      $disapline = 'Citizenship'  ;
    }
} else if ($citRank > $artRank ) {
    $disapline = 'Citizenship'  ;
}


# make query
$query = "
SELECT
resources.id, youtubeid, title, url, disciplines.name as discipline, indudtries.name as industry FROM `resources`
JOIN resources_disciplines ON resources.id = resources_disciplines.resource_id
JOIN disciplines ON disciplines.id = resources_disciplines.discipline_id
JOIN resources_indudtries ON resources_indudtries .resource_id =resources.id
JOIN indudtries ON indudtries.id = resources_indudtries .indudtry_id
WHERE disciplines.name  = '$disapline'
AND indudtries.name = '$industry'
";
$result = mysql_query($query);
mysql_close();

# print query
printdebug("<br/>$query<br/>")  ;

$num=mysql_numrows($result);
$i=0;
$url = '';
$title = '';
$id = '' ;
if($num > 0)
{
    $url =  mysql_result($result,$i,"url");
    $title =  mysql_result($result,$i,"title");
    $id =  mysql_result($result,$i,"youtubeid");
}
?>
<html>
<head>
<title>video template for <?php echo $disapline ?> - <?php echo $industry?></title>
</head>
<body>
<div style="text-align: center">

<h1><?php echo $disapline ?>: <?php echo $industry?></h1>
    <h2><?php echo $title;?></h2>

<iframe width="560" height="315" src="http://www.youtube.com/embed/<?php echo $id; ?>?autoplay=1" frameborder="0" allowfullscreen></iframe>
<p>

    <img src="reset.jpg" alt="reset" onClick="document.location.reload(true)" />
</p>
</div>
</body>

</html>

