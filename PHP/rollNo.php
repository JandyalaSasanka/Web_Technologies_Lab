<?php
      if ($_SERVER["REQUEST_METHOD"] == "POST") {
		   if (empty($_POST["rno"])) {
               $rnoErr = "Name is required";
			   echo $rnoErr;
			} else {
		    $rno =($_POST["rno"]);
			   $rno_arr=explode("-",$rno);
			   $val=$rno_arr[2];
			   if($val=='732')
				   echo 'Your Department is CIVIL';
			   elseif($val=='733')
			       echo 'Your Department is CSE';
			   elseif($val=='734')
			       echo 'Your Department is ECE';
               elseif($val=='735')
			       echo 'Your Department is EEE';
               elseif($val=='736')
			       echo 'Your Department is MECH';	
			    elseif($val=='737')
			       echo 'Your Department is IT';
				   
			}
	  }
?>