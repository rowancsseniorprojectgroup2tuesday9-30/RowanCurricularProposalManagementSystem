function openPage(pageName, elmnt, color) 
{
	if(pageName == "Home" || document.getElementById("department_name").text.includes("Department"))
	{
		var i, tabcontent, tablinks;
		tabcontent = document.getElementsByClassName("tabcontent");
		for (i = 0; i < tabcontent.length; i++) 
		{
			tabcontent[i].style.display = "none";
		}

		tablinks = document.getElementsByClassName("tablink");
		for (i = 0; i < tablinks.length; i++) 
		{
			tablinks[i].style.backgroundColor = "";
		}

		document.getElementById(pageName).style.display = "block";

		elmnt.style.backgroundColor = color;
	}
	else
	{
		alert("You must first login!");
	}
}

document.getElementById("defaultOpen").click();
	$(document).ready(function () 
		{
			document.getElementById("department_name").text = "";
			$('.check').css('stroke-dashoffset', 0);
		});

function fieldappear(that) 
{
    if (that.value == "form_A") 
	{
        document.getElementById("fadeableA").style.display = "block";
		document.getElementById("fadeableB").style.display = "none";
		document.getElementById("fadeableC").style.display = "none";
		document.getElementById("fadeableD").style.display = "none";
		document.getElementById("fadeableE").style.display = "none";
		document.getElementById("fadeableF").style.display = "none";
    } 
	else if (that.value == "form_B") 
	{
		document.getElementById("fadeableA").style.display = "none";
        document.getElementById("fadeableB").style.display = "block";
		document.getElementById("fadeableC").style.display = "none";
		document.getElementById("fadeableD").style.display = "none";
		document.getElementById("fadeableE").style.display = "none";
		document.getElementById("fadeableF").style.display = "none";
    } 
	else if (that.value == "form_C") 
	{
		document.getElementById("fadeableA").style.display = "none";
        document.getElementById("fadeableB").style.display = "none";
		document.getElementById("fadeableC").style.display = "block";
		document.getElementById("fadeableD").style.display = "none";
		document.getElementById("fadeableE").style.display = "none";
		document.getElementById("fadeableF").style.display = "none";
    } 
	else if (that.value == "form_D") 
	{
		document.getElementById("fadeableA").style.display = "none";
        document.getElementById("fadeableB").style.display = "none";
		document.getElementById("fadeableC").style.display = "none";
		document.getElementById("fadeableD").style.display = "block";
		document.getElementById("fadeableE").style.display = "none";
		document.getElementById("fadeableF").style.display = "none";
    } 
	else if (that.value == "form_E") 
	{
		document.getElementById("fadeableA").style.display = "none";
        document.getElementById("fadeableB").style.display = "none";
		document.getElementById("fadeableC").style.display = "none";
		document.getElementById("fadeableD").style.display = "none";
		document.getElementById("fadeableE").style.display = "block";
		document.getElementById("fadeableF").style.display = "none";
    } 
	else if (that.value == "form_F") 
	{
		document.getElementById("fadeableA").style.display = "none";
        document.getElementById("fadeableB").style.display = "none";
		document.getElementById("fadeableC").style.display = "none";
		document.getElementById("fadeableD").style.display = "none";
		document.getElementById("fadeableE").style.display = "none";
		document.getElementById("fadeableF").style.display = "block";
    } 
	else 
	{
        document.getElementById("fadeableA").style.display = "none";
		document.getElementById("fadeableB").style.display = "none";
		document.getElementById("fadeableC").style.display = "none";
		document.getElementById("fadeableD").style.display = "none";
		document.getElementById("fadeableE").style.display = "none";
		document.getElementById("fadeableF").style.display = "none";
    }
}

function mainappear(pass, dep, that) 
{
    if (pass.value == dep.value && pass.value != "") 
	{
        document.getElementById("fadeableMain").style.display = "block";
		document.getElementById("fadeableMain2").style.display = "none";
		document.getElementById("fadeableMain3").style.display = "block";
		document.getElementById("department_name").text = "Current Department: " + dep.value;
		document.getElementById("department_name2").text = "Current Department: " + dep.value;
		document.getElementById("department_name3").text = "Current Department: " + dep.value;
		document.getElementById("department_name4").text = "Current Department: " + dep.value;
		that.style.display = "none";
    } 
	else 
	{
		document.getElementById("fadeableMain").style.display = "none";
		document.getElementById("fadeableMain2").style.display = "block";
		document.getElementById("fadeableMain3").style.display = "none";
		alert("wrong password");
	}
	
}
