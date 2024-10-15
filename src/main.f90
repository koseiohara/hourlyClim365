program main

    use namelist, only : read_nml
    use clim    , only : hourly_clim_365

    implicit none

    real(4) :: clock_begin
    real(4) :: clock_end
    integer :: elapse_sec
    integer :: elapse_min
    integer :: elapse_hr

    call cpu_time(clock_begin)

    call read_nml()

    call hourly_clim_365()

    call cpu_time(clock_end)

    elapse_sec = int(clock_end-clock_begin)
    elapse_min = elapse_sec/60
    elapse_sec = elapse_sec-elapse_min*60
    elapse_hr  = elapse_min/60
    elapse_min = elapse_min-elapse_hr*60

    write(*,*)
    write(*,'(A)') 'PROCESS COMPLETE'
    write(*,'(A,I0,"hr ",I0,"min ",I0,"s")') 'EXECUTION TIME : ', elapse_hr, elapse_min , elapse_sec
    write(*,*)

end program main

