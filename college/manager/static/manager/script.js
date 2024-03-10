$('.form').find('input, textarea').on('keyup blur focus', function (e) {

  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight');
			} else {
		    label.removeClass('highlight');
			}
    } else if (e.type === 'focus') {

      if( $this.val() === '' ) {
    		label.removeClass('highlight');
			}
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

document.addEventListener('DOMContentLoaded', function() {
    changePlaceholder(document.querySelector('.tab.active a'));
});
function changePlaceholder(element) {
    const nameInput = document.getElementById('nameInput');
    const secondInput = document.getElementById('secondInput');
    const input_3 = document.getElementById('input_3');
    const input_4 = document.getElementById('input_4');
    const input_5 = document.getElementById('input_5');
    const actionInput = document.getElementById('action');

    if (element.textContent === 'New group') {
        nameInput.placeholder = "Name of the group";
        secondInput.placeholder = "Curator";
        input_3.placeholder = "Amount of students";
        input_4.placeholder = "Average score";
        input_5.placeholder = "Rating";
        actionInput.value = "group";
    } else if (element.textContent === 'New student') {
        nameInput.placeholder = "Name";
        secondInput.placeholder = "Surname";
        input_3.placeholder = "Group";
        input_4.placeholder = "Age";
        input_5.placeholder = "Average score";
        actionInput.value = "student";
    }

    const tabs = document.querySelectorAll('.tab');
    tabs.forEach(tab => {
        tab.classList.remove('active');
    });
    element.parentElement.classList.add('active');
}
