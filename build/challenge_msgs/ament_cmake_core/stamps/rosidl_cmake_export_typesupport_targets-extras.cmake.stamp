# generated from
# rosidl_cmake/cmake/template/rosidl_cmake_export_typesupport_targets.cmake.in

set(_exported_typesupport_targets
  "__rosidl_generator_c:challenge_msgs__rosidl_generator_c;__rosidl_typesupport_fastrtps_c:challenge_msgs__rosidl_typesupport_fastrtps_c;__rosidl_typesupport_introspection_c:challenge_msgs__rosidl_typesupport_introspection_c;__rosidl_typesupport_c:challenge_msgs__rosidl_typesupport_c;__rosidl_generator_cpp:challenge_msgs__rosidl_generator_cpp;__rosidl_typesupport_fastrtps_cpp:challenge_msgs__rosidl_typesupport_fastrtps_cpp;__rosidl_typesupport_introspection_cpp:challenge_msgs__rosidl_typesupport_introspection_cpp;__rosidl_typesupport_cpp:challenge_msgs__rosidl_typesupport_cpp;__rosidl_generator_py:challenge_msgs__rosidl_generator_py")

# populate challenge_msgs_TARGETS_<suffix>
if(NOT _exported_typesupport_targets STREQUAL "")
  # loop over typesupport targets
  foreach(_tuple ${_exported_typesupport_targets})
    string(REPLACE ":" ";" _tuple "${_tuple}")
    list(GET _tuple 0 _suffix)
    list(GET _tuple 1 _target)

    set(_target "challenge_msgs::${_target}")
    if(NOT TARGET "${_target}")
      # the exported target must exist
      message(WARNING "Package 'challenge_msgs' exports the typesupport target '${_target}' which doesn't exist")
    else()
      list(APPEND challenge_msgs_TARGETS${_suffix} "${_target}")
    endif()
  endforeach()
endif()
