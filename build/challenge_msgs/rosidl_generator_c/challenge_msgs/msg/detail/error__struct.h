// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from challenge_msgs:msg/Error.idl
// generated code does not contain a copyright notice

#ifndef CHALLENGE_MSGS__MSG__DETAIL__ERROR__STRUCT_H_
#define CHALLENGE_MSGS__MSG__DETAIL__ERROR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Error in the package challenge_msgs.
typedef struct challenge_msgs__msg__Error
{
  float center_error;
  float points_error;
} challenge_msgs__msg__Error;

// Struct for a sequence of challenge_msgs__msg__Error.
typedef struct challenge_msgs__msg__Error__Sequence
{
  challenge_msgs__msg__Error * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} challenge_msgs__msg__Error__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CHALLENGE_MSGS__MSG__DETAIL__ERROR__STRUCT_H_
