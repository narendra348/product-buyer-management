// static/js/main.js
function confirmDelete(type, id) {
  Swal.fire({
    title: 'Are you sure?',
    text: `You are about to delete this ${type}. This action cannot be undone.`,
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    confirmButtonText: 'Yes, delete it!'
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = `/delete/${type}/${id}`;
    }
  });
}

function filterList(type) {
  const input = document.getElementById(`search${type.charAt(0).toUpperCase() + type.slice(1)}`);
  const filter = input.value.toLowerCase();
  const list = document.getElementById(`${type}List`).getElementsByTagName('li');
  for (let i = 0; i < list.length; i++) {
    const item = list[i].getElementsByTagName('span')[0];
    const textValue = item.textContent || item.innerText;
    list[i].style.display = textValue.toLowerCase().indexOf(filter) > -1 ? '' : 'none';
  }
}

// Real-time form validation can be added here if needed
