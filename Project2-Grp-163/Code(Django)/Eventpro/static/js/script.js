const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSideMenu.forEach(i=> {
			i.parentElement.classList.remove('active');
		})
		li.classList.add('active');
	})
});


// TOGGLE SIDEBAR
//const menuBar = document.querySelector('#content nav .bx.bx-menu');
//const sidebar = document.getElementById('sidebar');

//menuBar.addEventListener('click', function () {
//	sidebar.classList.toggle('hide');
//})

const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
	if(window.innerWidth < 576) {
		e.preventDefault();
		searchForm.classList.toggle('show');
		if(searchForm.classList.contains('show')) {
			searchButtonIcon.classList.replace('bx-search', 'bx-x');
		} else {
			searchButtonIcon.classList.replace('bx-x', 'bx-search');
		}
	}
})





if(window.innerWidth < 768) {
	sidebar.classList.add('hide');
} else if(window.innerWidth > 576) {
	searchButtonIcon.classList.replace('bx-x', 'bx-search');
	searchForm.classList.remove('show');
}


window.addEventListener('resize', function () {
	if(this.innerWidth > 576) {
		searchButtonIcon.classList.replace('bx-x', 'bx-search');
		searchForm.classList.remove('show');
	}
})



const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
	if(this.checked) {
		document.body.classList.add('dark');
	} else {
		document.body.classList.remove('dark');
	}
})


document.querySelector("btns").addEventListener("click",function(){
	document.querySelector(".popup").classList.add("active");
});
document.querySelector(".popup").addEventListener("click",function(){
	document.querySelector("popup").classList.add("active");
});

function show1(){
	document.getElementById('popup1').style.height="510px"
	document.getElementById('popup1').style.display="block"
	document.getElementById('show1').style.display="none"
};

function hide1(){
	document.getElementById('popup1').style.height="0px"
	document.getElementById('popup1').style.display="none"
	document.getElementById('show1').style.display="inline"
};

function show2(){
	document.getElementById('popup2').style.height="510px"
	document.getElementById('popup2').style.display="block"
	document.getElementById('show2').style.display="none"
};

function hide2(){
	document.getElementById('popup2').style.height="0px"
	document.getElementById('popup2').style.display="none"
	document.getElementById('show2').style.display="inline"
};

function show3(){
	document.getElementById('popup3').style.height="510px"
	document.getElementById('popup3').style.display="block"
	document.getElementById('show3').style.display="none"
};

function hide3(){
	document.getElementById('popup3').style.height="0px"
	document.getElementById('popup3').style.display="none"
	document.getElementById('show3').style.display="inline"
};
function show4(){
	document.getElementById('popup4').style.height="510px"
	document.getElementById('popup4').style.display="block"
	document.getElementById('show4').style.display="none"
};

function hide4(){
	document.getElementById('popup4').style.height="0px"
	document.getElementById('popup4').style.display="none"
	document.getElementById('show4').style.display="inline"
};

function showc1(){
	document.getElementById('bahar1').style.height="510px"
	document.getElementById('bahar1').style.display="block"
	document.getElementById('showc1').style.display="none"
};

function hidec1(){
	document.getElementById('bahar1').style.height="0px"
	document.getElementById('bahar1').style.display="none"
	document.getElementById('showc1').style.display="inline"
};

function showc2(){
	document.getElementById('bahar2').style.height="510px"
	document.getElementById('bahar2').style.display="block"
	document.getElementById('showc2').style.display="none"
};

function hidec2(){
	document.getElementById('bahar2').style.height="0px"
	document.getElementById('bahar2').style.display="none"
	document.getElementById('showc2').style.display="inline"
};



