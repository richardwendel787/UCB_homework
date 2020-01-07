Sub StockMarket()
Dim SHEETNUMBER As Worksheet
    For Each SHEETNUMBER In ActiveWorkbook.Worksheets
    SHEETNUMBER.Activate
        
        LastRow = SHEETNUMBER.Cells(Rows.Count, 1).End(xlUp).Row
        
        Dim PercentageChange As Double
        Dim Ticker As String
        Dim StockVolume As Double
        Dim ChangeOnYear As Double
        Dim OpeningPrice As Double
        Dim ClosingPrice As Double

        Dim RowNumber As Double
        RowNumber = 2
        Dim ColumnNumber As Double
        ColumnNumber = 1
        Dim i As Long
        StockVolume = 0
        
        Cells(4, ColumnNumber + 15).Value = "Largest Percent Increase"
        Cells(5, ColumnNumber + 15).Value = "Largest Percent Decrease"
        Cells(6, ColumnNumber + 15).Value = "Largest StockVolume"
        Cells(3, ColumnNumber + 16).Value = "Ticker"
        Cells(3, ColumnNumber + 17).Value = "Value"

        Range("I9").Value = "Ticker"
        Range("J10").Value = "Year to Year Change"
        Range("K1").Value = "Percentage Change"
        Range("L12").Value = "Stock Volume"

        
        OpeningPrice = Cells(2, ColumnNumber + 2).Value
        
        
        For i = 2 To LastRow
        
            If Cells(i + 1, ColumnNumber).Value <> Cells(i, ColumnNumber).Value Then
               
                Ticker = Cells(i, ColumnNumber).Value
                Cells(RowNumber, ColumnNumber + 8).Value = Ticker
                
                ClosingPrice = Cells(i, ColumnNumber + 5).Value
                
                ChangeOnYear = ClosingPrice - OpeningPrice
                Cells(RowNumber, ColumnNumber + 9).Value = ChangeOnYear
                
                If (OpeningPrice = 0 And ClosingPrice = 0) Then
                    PercentageChange = 0
                ElseIf (OpeningPrice = 0 And ClosingPrice <> 0) Then
                    PercentageChange = 1
                Else
                    PercentageChange = ChangeOnYear / OpeningPrice
                    Cells(RowNumber, ColumnNumber + 10).Value = PercentageChange
                    Cells(RowNumber, ColumnNumber + 10).NumberFormat = "0%"
                End If
                
                StockVolume = StockVolume + Cells(i, ColumnNumber + 6).Value
                Cells(RowNumber, ColumnNumber + 11).Value = StockVolume
                
                RowNumber = RowNumber + 1
                OpeningPrice = Cells(i + 1, ColumnNumber + 2)
                StockVolume = 0
            
            Else
                StockVolume = StockVolume + Cells(i, ColumnNumber + 6).Value
            End If
        Next i
        
        YCLastRow = SHEETNUMBER.Cells(Rows.Count, ColumnNumber + 8).End(xlUp).Row
        For j = 2 To YCLastRow
            If (Cells(j, ColumnNumber + 9).Value > 0 Or Cells(j, ColumnNumber + 9).Value = 0) Then
                Cells(j, ColumnNumber + 9).Interior.ColorIndex = 10
            ElseIf Cells(j, ColumnNumber + 9).Value < 0 Then
                Cells(j, ColumnNumber + 9).Interior.ColorIndex = 3
            End If
        Next j
        
        For ROWVALUE = 2 To YCLastRow
            If Cells(ROWVALUE, ColumnNumber + 10).Value = Application.WorksheetFunction.Max(SHEETNUMBER.Range("K2:K" & YCLastRow)) Then
                Cells(4, ColumnNumber + 16).Value = Cells(ROWVALUE, ColumnNumber + 8).Value
                Cells(4, ColumnNumber + 17).Value = Cells(ROWVALUE, ColumnNumber + 10).Value
                Cells(4, ColumnNumber + 17).NumberFormat = "0.00%"
            ElseIf Cells(ROWVALUE, ColumnNumber + 10).Value = Application.WorksheetFunction.Min(SHEETNUMBER.Range("K2:K" & YCLastRow)) Then
                Cells(5, ColumnNumber + 16).Value = Cells(ROWVALUE, ColumnNumber + 8).Value
                Cells(5, ColumnNumber + 17).Value = Cells(ROWVALUE, ColumnNumber + 10).Value
                Cells(5, ColumnNumber + 17).NumberFormat = "0.00%"
            ElseIf Cells(ROWVALUE, ColumnNumber + 11).Value = Application.WorksheetFunction.Max(SHEETNUMBER.Range("L2:L" & YCLastRow)) Then
                Cells(6, ColumnNumber + 16).Value = Cells(ROWVALUE, ColumnNumber + 8).Value
                Cells(6, ColumnNumber + 17).Value = Cells(ROWVALUE, ColumnNumber + 11).Value
            End If
        Next ROWVALUE
    Next SHEETNUMBER
End Sub



