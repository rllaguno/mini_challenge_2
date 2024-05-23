// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from challenge_msgs:msg/Error.idl
// generated code does not contain a copyright notice
#include "challenge_msgs/msg/detail/error__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
challenge_msgs__msg__Error__init(challenge_msgs__msg__Error * msg)
{
  if (!msg) {
    return false;
  }
  // center_error
  // points_error
  return true;
}

void
challenge_msgs__msg__Error__fini(challenge_msgs__msg__Error * msg)
{
  if (!msg) {
    return;
  }
  // center_error
  // points_error
}

bool
challenge_msgs__msg__Error__are_equal(const challenge_msgs__msg__Error * lhs, const challenge_msgs__msg__Error * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // center_error
  if (lhs->center_error != rhs->center_error) {
    return false;
  }
  // points_error
  if (lhs->points_error != rhs->points_error) {
    return false;
  }
  return true;
}

bool
challenge_msgs__msg__Error__copy(
  const challenge_msgs__msg__Error * input,
  challenge_msgs__msg__Error * output)
{
  if (!input || !output) {
    return false;
  }
  // center_error
  output->center_error = input->center_error;
  // points_error
  output->points_error = input->points_error;
  return true;
}

challenge_msgs__msg__Error *
challenge_msgs__msg__Error__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  challenge_msgs__msg__Error * msg = (challenge_msgs__msg__Error *)allocator.allocate(sizeof(challenge_msgs__msg__Error), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(challenge_msgs__msg__Error));
  bool success = challenge_msgs__msg__Error__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
challenge_msgs__msg__Error__destroy(challenge_msgs__msg__Error * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    challenge_msgs__msg__Error__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
challenge_msgs__msg__Error__Sequence__init(challenge_msgs__msg__Error__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  challenge_msgs__msg__Error * data = NULL;

  if (size) {
    data = (challenge_msgs__msg__Error *)allocator.zero_allocate(size, sizeof(challenge_msgs__msg__Error), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = challenge_msgs__msg__Error__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        challenge_msgs__msg__Error__fini(&data[i - 1]);
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
challenge_msgs__msg__Error__Sequence__fini(challenge_msgs__msg__Error__Sequence * array)
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
      challenge_msgs__msg__Error__fini(&array->data[i]);
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

challenge_msgs__msg__Error__Sequence *
challenge_msgs__msg__Error__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  challenge_msgs__msg__Error__Sequence * array = (challenge_msgs__msg__Error__Sequence *)allocator.allocate(sizeof(challenge_msgs__msg__Error__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = challenge_msgs__msg__Error__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
challenge_msgs__msg__Error__Sequence__destroy(challenge_msgs__msg__Error__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    challenge_msgs__msg__Error__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
challenge_msgs__msg__Error__Sequence__are_equal(const challenge_msgs__msg__Error__Sequence * lhs, const challenge_msgs__msg__Error__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!challenge_msgs__msg__Error__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
challenge_msgs__msg__Error__Sequence__copy(
  const challenge_msgs__msg__Error__Sequence * input,
  challenge_msgs__msg__Error__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(challenge_msgs__msg__Error);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    challenge_msgs__msg__Error * data =
      (challenge_msgs__msg__Error *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!challenge_msgs__msg__Error__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          challenge_msgs__msg__Error__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!challenge_msgs__msg__Error__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
