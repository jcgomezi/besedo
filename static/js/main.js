function modify_register(id){
    let options = {
        method: 'GET',      
        headers: {},
      };
    fetch('get/?id='+id, options)
    .then(response => response.json())
    .then(body => {
        console.log(body)
        document.getElementById('modify_modal').classList.add('show')
        document.querySelector('body').classList.add('modal_open')
        form = document.getElementById('modify_form')
        form.querySelector('[name=id]').value = body[0].id
        form.querySelector('[name=first_name]').value = body[0].first_name
        form.querySelector('[name=last_name]').value = body[0].last_name
        form.querySelector('[name=email]').value = body[0].email
        form.querySelector('[name=phone]').value = body[0].phone
        form.querySelector('[name=age]').value = body[0].age
    });
}
async function delete_register(id){
    swal.fire({
      title: 'Delete register',
      text: "This action can't be undone, are you sure?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'yes, delete it!',
      cancelButtonText: 'No, cancel!',
      reverseButtons:true
    }).then((result) => {
      if (result.value) {
          const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
          let options = {
              method: 'POST',      
              headers: {'X-CSRFToken': csrftoken},
              body: JSON.stringify({
                      id: id,
      
              })
      
            };
            fetch('delete/', options)
            .then(response => response.json())
            .then(body => {
                if (body.hasOwnProperty('error')){
                  swal.fire({
                    icon: 'error',
                    title: 'Confirmation',
                    text: 'Error, please verify the data!'
                  })
                }
                else{
                  ask_for_initial_data();
                  swal.fire({
                    icon: 'success',
                    title: 'Confirmation',
                    text: 'Register deleted!'
                  })
                }
                });
          }
    })
    
}


async function ask_for_initial_data(){
    let options = {
        method: 'GET',      
        headers: {},
      };
      fetch('get/?all', options)
      .then(response => response.json())
      .then(body => {
          html_to_append = ''
          body.forEach(item => {
            html_to_append += '<tr>'
            html_to_append += '<td>'+item.id+'</td>'
            html_to_append += '<td>'+item.first_name+'</td>'
            html_to_append += '<td>'+item.last_name+'</td>'
            html_to_append += '<td>'+item.email+'</td>'
            html_to_append += '<td>'+item.phone+'</td>'
            html_to_append += '<td>'+item.age+'</td>'
            html_to_append += '<td><button class="btn btn-warning" onclick="modify_register('+item.id+')" type="button">Modify</button></td>'
            html_to_append += '<td><button class="btn btn-danger" onclick="delete_register('+item.id+')" type="button">Delete</button></td>'
            html_to_append += '</tr>'
          });
          document.getElementById('main_table_body').innerHTML = html_to_append
        // Do something with body
      });
}

ask_for_initial_data();



document.getElementById('add_new_register').addEventListener('click',function(){
  document.getElementById('add_modal').classList.add('show')
  document.querySelector('body').classList.add('modal_open')
})

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        let modals = document.getElementsByClassName('custom_modal')
        Array.from(modals).forEach(item => {item.classList.remove('show')})
        document.querySelector('body').classList.remove('modal_open')
    }
})

let close_buttons = document.getElementsByClassName('custom_modal_close')
Array.from(close_buttons).forEach(item => {item.addEventListener('click',function(){
    let modals = document.getElementsByClassName('custom_modal')
    Array.from(modals).forEach(item => {item.classList.remove('show')})
    document.querySelector('body').classList.remove('modal_open')
})})

document.getElementById('modify_form').addEventListener('submit',function(){
    swal.fire({
      title: 'Modify register',
      text: "This action can't be undone, are you sure?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'yes, update it!',
      cancelButtonText: 'No, cancel!',
      reverseButtons:true
    }).then((result) => {
      if (result.value) {
        let options = {
            method: 'POST',      
            headers: {'X-CSRFToken': this.elements.csrfmiddlewaretoken.value},
            body: JSON.stringify({
                    id: this.elements.id.value,
                    first_name: this.elements.first_name.value,    
                    last_name: this.elements.last_name.value,    
                    email: this.elements.email.value,    
                    phone: this.elements.phone.value,    
                    age: this.elements.age.value
            })
          };
          fetch('update/', options)
          .then(response => response.json())
          .then(body => {
              if (body.hasOwnProperty('error')){
                swal.fire({
                  icon: 'error',
                  title: 'Confirmation',
                  text: 'Error, please verify the data!'
                })
              }
              else{
                ask_for_initial_data();
                swal.fire({
                  icon: 'success',
                  title: 'Confirmation',
                  text: 'Register modified!'
                })
              }
          });
      }
    });
})

document.getElementById('add_form').addEventListener('submit',function(){
  swal.fire({
    title: 'Add register',
    text: "This action can't be undone, are you sure?",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonText: 'yes, add it!',
    cancelButtonText: 'No, cancel!',
    reverseButtons:true
  }).then((result) => {
    if (result.value) {
      let options = {
          method: 'POST',      
          headers: {'X-CSRFToken': this.elements.csrfmiddlewaretoken.value},
          body: JSON.stringify({
                  first_name: this.elements.first_name.value,    
                  last_name: this.elements.last_name.value,    
                  email: this.elements.email.value,    
                  phone: this.elements.phone.value,    
                  age: this.elements.age.value
          })
        };
        fetch('insert/', options)
        .then(response => response.json())
        .then(body => {
            if (body.hasOwnProperty('error')){
              swal.fire({
                icon: 'error',
                title: 'Confirmation',
                text: 'Error, please verify the data!'
              })
            }
            else{
              ask_for_initial_data();
              swal.fire({
                icon: 'success',
                title: 'Confirmation',
                text: 'Register added!'
              })
            }
        });
    }
  });
})