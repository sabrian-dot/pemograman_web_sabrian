function fungsi1(e){
    elemen = e.currentTarget;
    console.log(elemen)
    var nama = "sabrian";
    document.getElementById("nama").innerHTML = " " + nama;
    
}

function fungsi2(e){
    elemen = e.currentTarget;
    var nama1 = "ADI";
    document.getElementById("nama").innerHTML = "  " + nama1;
}

function reset(){
    document.getElementById("nama").innerHTML ="";
}

function fungsi3(e){
    elemen = e.currentTarget;
    console.log(elemen)
    var nama = "sabrian";
    document.getElementById("nama").innerHTML = "nama saya adalah " + nama;
    
}

function fungsi4(e){
    elemen = e.currentTarget;
    var nama1 = "ADI";
    document.getElementById("nama2").innerHTML = "nama saya adalah  " + nama1;
}

const display = document.getElementById('nama');

function fungsi5(event) {
    display.innerText = "nama saya adalah sabrian";
    
    event.target.onmouseout = function() {
        display.innerText = "";
    };
}

function fungsi6(event) {
    display.innerText = "nama saya adalah ADI"; 
    
    event.target.onmouseout = function() {
        display.innerText = "";
    };
}

function tambah() {
    let a = parseInt(document.getElementById("nilaiA").value);
    let b = parseInt(document.getElementById("nilaiB").value);

    let hasil = a + b;

    document.getElementById("hasil").innerHTML = hasil;
}

function setOperator(op) {
    operator = op;
}

function hitung(e) {
    e.preventDefault();

    let a = parseInt(document.getElementById("angka1").value);
    let b = parseInt(document.getElementById("angka2").value);
    let hasil = 0;

    if (operator === "+") {
        hasil = a + b;
    } else if (operator === "-") {
        hasil = a - b;
    }

    document.getElementById("hasil").innerHTML =
        "<p><b>Hasil: " + hasil + "</b></p>";
}

 function setOperator(op) {
            operator = op;
        }

        function Kalkulator(e) {
            e.preventDefault();

            let a = parseFloat(document.getElementById("angka1").value);
            let b = parseFloat(document.getElementById("angka2").value);
            let hasil;

            if (operator === "+") {
                hasil = a + b;
            } else if (operator === "-") {
                hasil = a - b;
            } else if (operator === "*") {
                hasil = a * b;
            } else if (operator === "/") {
                if (b === 0) {
                    hasil = "Tidak bisa dibagi 0";
                } else {
                    hasil = a / b;
                }
            }

            document.getElementById("hasil").innerHTML =
                "<p><b>Hasil: " + hasil + "</b></p>";
        }

        let mode = "dolar"; 

function konversi() {
    let nilai = parseFloat(document.getElementById("nilai").value);
    let hasil = 0;

    if (mode === "dolar") {
        hasil = nilai * 16000;
        document.getElementById("hasil").innerHTML =
            "Rupiah " + hasil;
    } else {
        hasil = nilai / 16000;
        document.getElementById("hasil").innerHTML =
            "Dollar " + hasil;
    }
}

function tukar() {
    let label = document.getElementById("label");
    let hasil = document.getElementById("hasil");

    if (mode === "dolar") {
        mode = "rupiah";
        label.innerHTML = "Rupiah";
        hasil.innerHTML = "Dollar 1";
        document.getElementById("nilai").value = 16000;
    } else {
        mode = "dolar";
        label.innerHTML = "Dollar";
        hasil.innerHTML = "Rupiah 15000";
        document.getElementById("nilai").value = 1;
    }
}
let timer = null;

function konversi2() {
    clearTimeout(timer);

    timer = setTimeout(() => {
        let c = document.getElementById("celcius").value;

        if (c === "") {
            document.getElementById("hasil").innerHTML = "Fahrenheit";
            return;
        }

        let f = (c * 9 / 5) + 32;

        document.getElementById("hasil").innerHTML =
            "Fahrenheit " + f;
    }, 500); 
}

function cekKelulusan() {
    let batas = parseInt(document.getElementById("batas").value);
    let nilai = parseInt(document.getElementById("nilai").value);
    let hasil = document.getElementById("hasil");

    if (isNaN(nilai) || isNaN(batas)) {
        hasil.innerHTML = "Masukkan nilai dengan benar";
        return;
    }

    if (nilai >= batas) {
        hasil.innerHTML = "Lulus";
    } else {
        hasil.innerHTML = "Tidak Lulus";
    }
}

const btnUtama = document.getElementById('btnUtama');
const containerMenu = document.getElementById('containerMenu');


btnUtama.onclick = function() {
   
    if (containerMenu.style.display === 'none') {
        containerMenu.style.display = 'block';
    } else {
        containerMenu.style.display = 'none';
    }
};




