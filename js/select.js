function check()
{
    var Teach=document.getElementById("Tea").checked;
    var Stu=document.getElementById("St").checked;
    
    if(Boolean(Teach))
    {
        document.getElementById("tea_login").style.display="block";
        document.getElementById("stu_login").style.display="none";
        document.getElementById("lolipop").style.display="none";
    }
    if(Boolean(Stu))
    {    
        document.getElementById("tea_login").style.display="none";
        document.getElementById("stu_login").style.display="block";
        document.getElementById("lolipop").style.display="none";    
    }
    var errormsg=error.message;
    window.alert("Error:"+errormsg);
}