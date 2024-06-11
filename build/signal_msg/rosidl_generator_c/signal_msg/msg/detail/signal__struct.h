// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from signal_msg:msg/Signal.idl
// generated code does not contain a copyright notice

#ifndef SIGNAL_MSG__MSG__DETAIL__SIGNAL__STRUCT_H_
#define SIGNAL_MSG__MSG__DETAIL__SIGNAL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Signal in the package signal_msg.
typedef struct signal_msg__msg__Signal
{
  rosidl_runtime_c__String name;
  int32_t num;
  float reliability;
} signal_msg__msg__Signal;

// Struct for a sequence of signal_msg__msg__Signal.
typedef struct signal_msg__msg__Signal__Sequence
{
  signal_msg__msg__Signal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} signal_msg__msg__Signal__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIGNAL_MSG__MSG__DETAIL__SIGNAL__STRUCT_H_
