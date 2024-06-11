// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from yolo_msg:msg/Yolov8Inference.idl
// generated code does not contain a copyright notice

#ifndef YOLO_MSG__MSG__DETAIL__YOLOV8_INFERENCE__STRUCT_H_
#define YOLO_MSG__MSG__DETAIL__YOLOV8_INFERENCE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'yolov8_inference'
#include "yolo_msg/msg/detail/inference_result__struct.h"

/// Struct defined in msg/Yolov8Inference in the package yolo_msg.
typedef struct yolo_msg__msg__Yolov8Inference
{
  std_msgs__msg__Header header;
  yolo_msg__msg__InferenceResult__Sequence yolov8_inference;
} yolo_msg__msg__Yolov8Inference;

// Struct for a sequence of yolo_msg__msg__Yolov8Inference.
typedef struct yolo_msg__msg__Yolov8Inference__Sequence
{
  yolo_msg__msg__Yolov8Inference * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} yolo_msg__msg__Yolov8Inference__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // YOLO_MSG__MSG__DETAIL__YOLOV8_INFERENCE__STRUCT_H_
