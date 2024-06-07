// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from yolo_msg:msg/Yolov8Inference.idl
// generated code does not contain a copyright notice

#ifndef YOLO_MSG__MSG__DETAIL__YOLOV8_INFERENCE__TRAITS_HPP_
#define YOLO_MSG__MSG__DETAIL__YOLOV8_INFERENCE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "yolo_msg/msg/detail/yolov8_inference__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'yolov8_inference'
#include "yolo_msg/msg/detail/inference_result__traits.hpp"

namespace yolo_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const Yolov8Inference & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: yolov8_inference
  {
    if (msg.yolov8_inference.size() == 0) {
      out << "yolov8_inference: []";
    } else {
      out << "yolov8_inference: [";
      size_t pending_items = msg.yolov8_inference.size();
      for (auto item : msg.yolov8_inference) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Yolov8Inference & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: yolov8_inference
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.yolov8_inference.size() == 0) {
      out << "yolov8_inference: []\n";
    } else {
      out << "yolov8_inference:\n";
      for (auto item : msg.yolov8_inference) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Yolov8Inference & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace yolo_msg

namespace rosidl_generator_traits
{

[[deprecated("use yolo_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const yolo_msg::msg::Yolov8Inference & msg,
  std::ostream & out, size_t indentation = 0)
{
  yolo_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use yolo_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const yolo_msg::msg::Yolov8Inference & msg)
{
  return yolo_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<yolo_msg::msg::Yolov8Inference>()
{
  return "yolo_msg::msg::Yolov8Inference";
}

template<>
inline const char * name<yolo_msg::msg::Yolov8Inference>()
{
  return "yolo_msg/msg/Yolov8Inference";
}

template<>
struct has_fixed_size<yolo_msg::msg::Yolov8Inference>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<yolo_msg::msg::Yolov8Inference>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<yolo_msg::msg::Yolov8Inference>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // YOLO_MSG__MSG__DETAIL__YOLOV8_INFERENCE__TRAITS_HPP_
