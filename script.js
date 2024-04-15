var buttons = document.querySelectorAll('button');

buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        var fileInput = document.createElement('input');
        fileInput.type = 'file';
        if (button.id === 'button5' || button.id === 'button6') {
            fileInput.accept = '.mp3,.wav,.ogg';
        } else if (button.id === 'button4') {
            fileInput.accept = '.jpg,.jpeg,.png,.gif';
        } else {
            fileInput.accept = '.txt';
        }
        fileInput.onchange = function(event) {
            // Handle file upload here
        };
        if (button.id!== 'theme-button') {
            fileInput.click();
        }
    });
});

document.getElementById('theme-button').addEventListener('click', function() {
    var body = document.body;
    var themeButton = document.getElementById('theme-button');
    if (body.style.backgroundColor === 'white') {
        body.style.backgroundColor = '#333';
        themeButton.style.backgroundColor = '#333';
        themeButton.style.color = 'white';
        document.querySelectorAll('button').forEach(function(button) {
            button.style.backgroundColor = '#333';
            button.style.color = 'white';
        });
    } else {
        body.style.backgroundColor = 'white';
        themeButton.style.backgroundColor = 'black';
        themeButton.style.color = 'white';
        document.querySelectorAll('button').forEach(function(button) {
            button.style.backgroundColor = 'white';
            button.style.color = 'black';
        });
    }
});
function changeTheme() {
    const themeButton = document.getElementById("theme-button");
    const body = document.body;
    if (body.style.backgroundColor === 'white') {
      themeButton.textContent = "Night";
    } else {
      themeButton.textContent = "Light";
    }
  }