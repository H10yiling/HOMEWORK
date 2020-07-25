<!DOCTYPE html>
<html>
<head>
	<title>registeredtest0720</title>
</head>
<body>
	<?php
	$link = mysqli_connect("localhost","root","","demo");
	if(!$link)
		echo "連接失敗";
	$sql = "set names utf8";
    mysqli_query($link,$sql);
	$edit = "";
	if(isset($_POST["edit"]))
		$edit = key($_POST["edit"]);
	if(isset($_POST["post"]))
	{
		$sql = "INSERT INTO registeredtest0720
		                   (NAME,
		                    BIRTHDAY,
		                    AGE)
		             VALUES('".$_POST["name"]."',
		                    '".$_POST["birthday"]."',
		                    '".$_POST["age"]."')";
		mysqli_query($link,$sql);
	}
	if (isset($_POST["save"]))
	{
		$sql = "UPDATE `registeredtest0720` 
				   SET `NAME` = '".$_POST["edit_name"]."',
				       `BIRTHDAY` = '".$_POST["edit_birthday"]."',
				       `AGE` = '".$_POST["edit_age"]."'
				 WHERE `registeredtest0720`.`ID` = ".key($_POST["save"]);
		mysqli_query($link,$sql);
	}
	if (isset($_POST['delete']))
	{
		$sql = "DELETE FROM `registeredtest0720` 
				 	  WHERE `registeredtest0720`.`ID` = ".key($_POST['delete']);
		mysqli_query($link,$sql);
	}
    if(isset($_POST["delete_all"]))
    {
        for($i=0;$i<count($_POST["no"]);$i++)
        {
            $sql = "DELETE FROM `registeredtest0720` 
                          WHERE `registeredtest0720`.`ID` = ".$_POST["no"][$i];
            mysqli_query($link,$sql);
        }
    }
	?>
	<form method="post">
			<h1 style="color: #FAFAFA; background: #969696	">註冊</h1>
			<h4>NAME：<input type="text" name="name"></h4>
			<h4>BIRTHDAY：<input type="text" name="birthday"> ( EX:19870807 )</h4>
			<h4>AGE：<input type="text" name="age"></h4>
			<input type="submit" name="post" value="提交">
			<hr>
		<table width="500" border="1" align="center">
			<tr>
                <td colspan="10">
                    <input type="submit" name="delete_all" value="勾選刪除">
                </td>
            </tr>
			<tr>
				<td>選</td>
				<td>功能</td>
				<td>註冊者</td>
				<td>生日</td>
				<td>年齡</td>
				<td>時間</td>
			</tr>
			<?php
			$sql = "select ID,
							NAME,
			            	BIRTHDAY,
			            	AGE,
			            	TIME
			          from registeredtest0720";
			$result = mysqli_query($link,$sql);
			while($row = mysqli_fetch_assoc($result))
			{
				echo "<tr>";
				echo "<td><input type='checkbox' name='no[]' value='".$row["ID"]."'></td>";
				echo "<td>";
					if ($row["ID"]==$edit)
						echo "<input type='submit' name='save[".$row["ID"]."]' value='存'>";
					else
					{
						echo "<input type='submit' name='edit[".$row["ID"]."]' value='編'>";
						echo "<input type='submit' name='delete[".$row["ID"]."]' value='刪'>";
					}
				echo "</td>";
				echo "<td>";
					if($row["ID"]==$edit)
						echo "<input type='text' size=10 name='edit_name' value='".$row["NAME"].	"'>";
					else
						echo $row["NAME"];
				echo "</td>";
				echo "<td>";
					if($row["ID"]==$edit)
						echo "<input type='text' size=10 name='edit_birthday' value='".$row["BIRTHDAY"]."'>";
					else
						echo $row["BIRTHDAY"];
				echo "</td>";
				echo "<td>";
					if($row["ID"]==$edit)
						echo "<input type='text' size=10 name='edit_age' value='".$row["AGE"]."'>";
					else
						echo $row["AGE"];
				echo "</td>";
				echo "<td>".$row["TIME"]."</td>";
				echo "</tr>";
			}
			?>
		</table>
	</form>
</body>
</html>