window.onload = function(){
  showArea();
  closeArea();
};

function showArea(){
  var area_btn = document.getElementsByClassName("menu-btn");
  for (var i = 0; i < area_btn.length; i++) {
    area_btn[i].onclick = function(){
      var area_id = this.dataset.showArea;
      document.getElementById("full-area").classList.add("show-full-box");
      document.getElementById(area_id).classList.add("show-full-box");
    };
  };
};

function closeArea(){
  var cancel_btn = document.getElementsByClassName("cancel-btn");
  for (var i = 0; i < cancel_btn.length; i++) {
    cancel_btn[i].onclick = function(){
      var contents = document.getElementsByClassName("full-content");
      for (var i = 0; i < contents.length; i++) {
        contents[i].classList.remove("show-full-box");
      };
      document.getElementById("full-area").classList.remove("show-full-box");
    };
  };
};
