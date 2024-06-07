// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from yolo_msg:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#ifndef YOLO_MSG__MSG__DETAIL__INFERENCE_RESULT__BUILDER_HPP_
#define YOLO_MSG__MSG__DETAIL__INFERENCE_RESULT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "yolo_msg/msg/detail/inference_result__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace yolo_msg
{

namespace msg
{

namespace builder
{

class Init_InferenceResult_right
{
public:
  explicit Init_InferenceResult_right(::yolo_msg::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  ::yolo_msg::msg::InferenceResult right(::yolo_msg::msg::InferenceResult::_right_type arg)
  {
    msg_.right = std::move(arg);
    return std::move(msg_);
  }

private:
  ::yolo_msg::msg::InferenceResult msg_;
};

class Init_InferenceResult_bottom
{
public:
  explicit Init_InferenceResult_bottom(::yolo_msg::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  Init_InferenceResult_right bottom(::yolo_msg::msg::InferenceResult::_bottom_type arg)
  {
    msg_.bottom = std::move(arg);
    return Init_InferenceResult_right(msg_);
  }

private:
  ::yolo_msg::msg::InferenceResult msg_;
};

class Init_InferenceResult_left
{
public:
  explicit Init_InferenceResult_left(::yolo_msg::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  Init_InferenceResult_bottom left(::yolo_msg::msg::InferenceResult::_left_type arg)
  {
    msg_.left = std::move(arg);
    return Init_InferenceResult_bottom(msg_);
  }

private:
  ::yolo_msg::msg::InferenceResult msg_;
};

class Init_InferenceResult_top
{
public:
  explicit Init_InferenceResult_top(::yolo_msg::msg::InferenceResult & msg)
  : msg_(msg)
  {}
  Init_InferenceResult_left top(::yolo_msg::msg::InferenceResult::_top_type arg)
  {
    msg_.top = std::move(arg);
    return Init_InferenceResult_left(msg_);
  }

private:
  ::yolo_msg::msg::InferenceResult msg_;
};

class Init_InferenceResult_class_name
{
public:
  Init_InferenceResult_class_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InferenceResult_top class_name(::yolo_msg::msg::InferenceResult::_class_name_type arg)
  {
    msg_.class_name = std::move(arg);
    return Init_InferenceResult_top(msg_);
  }

private:
  ::yolo_msg::msg::InferenceResult msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::yolo_msg::msg::InferenceResult>()
{
  return yolo_msg::msg::builder::Init_InferenceResult_class_name();
}

}  // namespace yolo_msg

#endif  // YOLO_MSG__MSG__DETAIL__INFERENCE_RESULT__BUILDER_HPP_
