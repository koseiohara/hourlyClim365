module debugger

    use BinIO, only : finfo, get_record

    implicit none

    private
    public :: debug_open, debug_close, debug_write, debug_linebreak

    integer :: dunit

    contains


    subroutine debug_open()

        open(unit=dunit, file='../output/debugger.txt')

    end subroutine debug_open


    subroutine debug_close()

        close(dunit)

    end subroutine debug_close


    subroutine debug_write(ftype)
        type(finfo), intent(in) :: ftype

        integer :: record

        call get_record(ftype , &  !! IN
                      & record  )  !! OUT

        write(dunit,'(I9,",")',ADVANCE='NO') record

    end subroutine debug_write


    subroutine debug_linebreak()

        write(dunit,*)

    end subroutine debug_linebreak


end module debugger

