# function to print a noticeable message
function(notice_message msg)
    message(STATUS "-------------------------------")
    message(STATUS "${CMAKE_PROJECT_NAME}:")
    message(STATUS "     ${msg}")
    message(STATUS "-------------------------------")
endfunction()