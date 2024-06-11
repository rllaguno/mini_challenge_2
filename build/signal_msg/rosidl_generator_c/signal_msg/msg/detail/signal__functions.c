// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from signal_msg:msg/Signal.idl
// generated code does not contain a copyright notice
#include "signal_msg/msg/detail/signal__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"

bool
signal_msg__msg__Signal__init(signal_msg__msg__Signal * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    signal_msg__msg__Signal__fini(msg);
    return false;
  }
  // num
  // reliability
  return true;
}

void
signal_msg__msg__Signal__fini(signal_msg__msg__Signal * msg)
{
  if (!msg) {
    return;
  }
  // name
  rosidl_runtime_c__String__fini(&msg->name);
  // num
  // reliability
}

bool
signal_msg__msg__Signal__are_equal(const signal_msg__msg__Signal * lhs, const signal_msg__msg__Signal * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // num
  if (lhs->num != rhs->num) {
    return false;
  }
  // reliability
  if (lhs->reliability != rhs->reliability) {
    return false;
  }
  return true;
}

bool
signal_msg__msg__Signal__copy(
  const signal_msg__msg__Signal * input,
  signal_msg__msg__Signal * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // num
  output->num = input->num;
  // reliability
  output->reliability = input->reliability;
  return true;
}

signal_msg__msg__Signal *
signal_msg__msg__Signal__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  signal_msg__msg__Signal * msg = (signal_msg__msg__Signal *)allocator.allocate(sizeof(signal_msg__msg__Signal), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(signal_msg__msg__Signal));
  bool success = signal_msg__msg__Signal__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
signal_msg__msg__Signal__destroy(signal_msg__msg__Signal * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    signal_msg__msg__Signal__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
signal_msg__msg__Signal__Sequence__init(signal_msg__msg__Signal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  signal_msg__msg__Signal * data = NULL;

  if (size) {
    data = (signal_msg__msg__Signal *)allocator.zero_allocate(size, sizeof(signal_msg__msg__Signal), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = signal_msg__msg__Signal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        signal_msg__msg__Signal__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
signal_msg__msg__Signal__Sequence__fini(signal_msg__msg__Signal__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      signal_msg__msg__Signal__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

signal_msg__msg__Signal__Sequence *
signal_msg__msg__Signal__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  signal_msg__msg__Signal__Sequence * array = (signal_msg__msg__Signal__Sequence *)allocator.allocate(sizeof(signal_msg__msg__Signal__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = signal_msg__msg__Signal__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
signal_msg__msg__Signal__Sequence__destroy(signal_msg__msg__Signal__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    signal_msg__msg__Signal__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
signal_msg__msg__Signal__Sequence__are_equal(const signal_msg__msg__Signal__Sequence * lhs, const signal_msg__msg__Signal__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!signal_msg__msg__Signal__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
signal_msg__msg__Signal__Sequence__copy(
  const signal_msg__msg__Signal__Sequence * input,
  signal_msg__msg__Signal__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(signal_msg__msg__Signal);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    signal_msg__msg__Signal * data =
      (signal_msg__msg__Signal *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!signal_msg__msg__Signal__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          signal_msg__msg__Signal__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!signal_msg__msg__Signal__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
