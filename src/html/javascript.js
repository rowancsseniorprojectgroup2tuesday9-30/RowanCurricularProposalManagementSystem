function openPage(pageName, elmnt, color) 
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

document.getElementById("defaultOpen").click();

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
		document.getElementById("department_name").text = dep.value;
		that.style.display = "none";
    } 
	else 
	{
		document.getElementById("fadeableMain").style.display = "none";
		document.getElementById("fadeableMain2").style.display = "block";
		alert("wrong password");
	}
	
}
