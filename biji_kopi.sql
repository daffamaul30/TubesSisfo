-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 03, 2020 at 08:47 AM
-- Server version: 5.7.29-0ubuntu0.18.04.1
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kopi`
--

-- --------------------------------------------------------

--
-- Table structure for table `biaya`
--

CREATE TABLE `biaya` (
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL,
  `berat_kg` int(10) NOT NULL,
  `biaya` int(20) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `biaya`
--

INSERT INTO `biaya` (`id_biaya`, `berat_kg`, `biaya`, `tanggal`) VALUES
(0000000012, 15, 15000, '2020-05-02'),
(0000000013, 10, 1000, '2020-05-03'),
(0000000016, 14, 18000, '2020-05-02'),
(0000000017, 15, 12000, '2020-05-02'),
(0000000018, 3, 50000, '2020-05-03'),
(0000000019, 3, 23000, '2020-05-04'),
(0000000025, 12, 44000, '2020-05-05'),
(0000000026, 15, 20000, '2020-05-06'),
(0000000027, 12, 40000, '2020-05-06'),
(0000000033, 150, 120000, '2020-05-03'),
(0000000034, 180, 1200000, '2020-05-03'),
(0000000035, 150, 260000, '2020-05-03'),
(0000000036, 110, 200000, '2020-05-03'),
(0000000037, 100, 180000, '2020-05-03'),
(0000000038, 90, 160000, '2020-05-03'),
(0000000039, 80, 130000, '2020-05-03'),
(0000000040, 70, 120000, '2020-05-03'),
(0000000041, 60, 156000, '2020-05-03'),
(0000000042, 50, 153000, '2020-05-03'),
(0000000044, 69, 696969, '2020-05-03'),
(0000000045, 500, 500, '2020-05-04'),
(0000000046, 12, 12, '2020-05-04');

-- --------------------------------------------------------

--
-- Table structure for table `bongkar`
--

CREATE TABLE `bongkar` (
  `id_bongkar` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_gabahB` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bongkar`
--

INSERT INTO `bongkar` (`id_bongkar`, `id_gabahB`, `id_biaya`) VALUES
(0000000001, 0000000001, 0000000017),
(0000000002, 0000000002, 0000000036);

-- --------------------------------------------------------

--
-- Table structure for table `cherry`
--

CREATE TABLE `cherry` (
  `id_cherry` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_panen` int(10) UNSIGNED ZEROFILL NOT NULL,
  `jumlah_kg` int(10) NOT NULL,
  `harga_kg` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cherry`
--

INSERT INTO `cherry` (`id_cherry`, `id_panen`, `jumlah_kg`, `harga_kg`) VALUES
(0000000001, 0000000002, 100, 20000),
(0000000002, 0000000003, 12, 10000),
(0000000003, 0000000004, 10, 1000000),
(0000000004, 0000000005, 190, 2301921),
(0000000005, 0000000006, 12, 1000),
(0000000006, 0000000007, 200, 100000),
(0000000007, 0000000008, 200, 1000000),
(0000000008, 0000000009, 500, 500),
(0000000009, 0000000010, 12, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `gabah_basah`
--

CREATE TABLE `gabah_basah` (
  `id_gabahB` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_cherry` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `gabah_basah`
--

INSERT INTO `gabah_basah` (`id_gabahB`, `id_cherry`) VALUES
(0000000001, 0000000001),
(0000000002, 0000000007);

-- --------------------------------------------------------

--
-- Table structure for table `gabah_kering`
--

CREATE TABLE `gabah_kering` (
  `id_gabahK` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_gabahB` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `gabah_kering`
--

INSERT INTO `gabah_kering` (`id_gabahK`, `id_gabahB`) VALUES
(0000000001, 0000000001),
(0000000002, 0000000002);

-- --------------------------------------------------------

--
-- Table structure for table `grading`
--

CREATE TABLE `grading` (
  `id_grading` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_bean` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `grading`
--

INSERT INTO `grading` (`id_grading`, `id_bean`, `id_biaya`) VALUES
(0000000001, 0000000001, 0000000026),
(0000000002, 0000000002, 0000000041);

-- --------------------------------------------------------

--
-- Table structure for table `green_bean`
--

CREATE TABLE `green_bean` (
  `id_bean` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_gabahK` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `green_bean`
--

INSERT INTO `green_bean` (`id_bean`, `id_gabahK`) VALUES
(0000000001, 0000000001),
(0000000002, 0000000002);

-- --------------------------------------------------------

--
-- Table structure for table `hand_pick`
--

CREATE TABLE `hand_pick` (
  `id_hand_pick` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_bean` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hand_pick`
--

INSERT INTO `hand_pick` (`id_hand_pick`, `id_bean`, `id_biaya`) VALUES
(0000000007, 0000000002, 0000000044);

-- --------------------------------------------------------

--
-- Table structure for table `hull`
--

CREATE TABLE `hull` (
  `id_hull` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_gabahK` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hull`
--

INSERT INTO `hull` (`id_hull`, `id_gabahK`, `id_biaya`) VALUES
(0000000001, 0000000001, 0000000019),
(0000000002, 0000000002, 0000000038);

-- --------------------------------------------------------

--
-- Table structure for table `jemurB`
--

CREATE TABLE `jemurB` (
  `id_jemurB` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_gabahB` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jemurB`
--

INSERT INTO `jemurB` (`id_jemurB`, `id_gabahB`, `id_biaya`) VALUES
(0000000001, 0000000001, 0000000018),
(0000000002, 0000000002, 0000000037);

-- --------------------------------------------------------

--
-- Table structure for table `jemurK`
--

CREATE TABLE `jemurK` (
  `id_jemurK` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_gabahK` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jemurK`
--

INSERT INTO `jemurK` (`id_jemurK`, `id_gabahK`, `id_biaya`) VALUES
(0000000001, 0000000002, 0000000039);

-- --------------------------------------------------------

--
-- Table structure for table `panen`
--

CREATE TABLE `panen` (
  `id_panen` int(10) UNSIGNED ZEROFILL NOT NULL,
  `tanggal` date NOT NULL,
  `blok` varchar(50) NOT NULL,
  `varietas` varchar(50) NOT NULL,
  `tipe_proses` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'cherry'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `panen`
--

INSERT INTO `panen` (`id_panen`, `tanggal`, `blok`, `varietas`, `tipe_proses`, `status`) VALUES
(0000000002, '2020-05-01', 'A', 'Kopi Arabica', 'Full Wash', 'green_color'),
(0000000003, '2020-05-02', 'V', 'Kopi Robusta', 'Full Wash', 'cherry'),
(0000000004, '2020-05-03', 'F', 'Kopi Luwak', 'Full Wash', 'cherry'),
(0000000005, '2020-05-14', 'ASS', 'Kopi Arabica', 'Wet Hull', 'cherry'),
(0000000006, '2020-05-02', 'kamu', 'Kopi Robusta', 'Full Wash', 'wetmill'),
(0000000007, '2020-05-03', 'Q', 'Kopi Arabica', 'Wet Hull', 'wetmill'),
(0000000008, '2020-05-03', 'W', 'Kopi Arabica', 'Natural Wet Hull', 'green_hand_pick'),
(0000000009, '2020-05-03', 'A', 'Kopi Robusta', 'Full Wash', 'wetmill'),
(0000000010, '2020-05-03', 'dia', 'Kopi Robusta', 'Full Wash', 'wetmill');

-- --------------------------------------------------------

--
-- Table structure for table `sorter`
--

CREATE TABLE `sorter` (
  `id_sorter` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_bean` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sorter`
--

INSERT INTO `sorter` (`id_sorter`, `id_bean`, `id_biaya`) VALUES
(0000000001, 0000000001, 0000000027),
(0000000002, 0000000002, 0000000042);

-- --------------------------------------------------------

--
-- Table structure for table `suton`
--

CREATE TABLE `suton` (
  `id_suton` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_bean` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `suton`
--

INSERT INTO `suton` (`id_suton`, `id_bean`, `id_biaya`) VALUES
(0000000001, 0000000001, 0000000025),
(0000000002, 0000000002, 0000000040);

-- --------------------------------------------------------

--
-- Table structure for table `transport`
--

CREATE TABLE `transport` (
  `id_transport` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_gabahB` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transport`
--

INSERT INTO `transport` (`id_transport`, `id_gabahB`, `id_biaya`) VALUES
(0000000001, 0000000001, 0000000016),
(0000000002, 0000000002, 0000000035);

-- --------------------------------------------------------

--
-- Table structure for table `wetmill`
--

CREATE TABLE `wetmill` (
  `id_wetmill` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_cherry` int(10) UNSIGNED ZEROFILL NOT NULL,
  `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wetmill`
--

INSERT INTO `wetmill` (`id_wetmill`, `id_cherry`, `id_biaya`) VALUES
(0000000002, 0000000001, 0000000012),
(0000000003, 0000000001, 0000000013),
(0000000004, 0000000001, 0000000033),
(0000000005, 0000000007, 0000000034),
(0000000006, 0000000008, 0000000045),
(0000000007, 0000000001, 0000000046);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `biaya`
--
ALTER TABLE `biaya`
  ADD PRIMARY KEY (`id_biaya`);

--
-- Indexes for table `bongkar`
--
ALTER TABLE `bongkar`
  ADD PRIMARY KEY (`id_bongkar`),
  ADD KEY `bongkarFK1` (`id_gabahB`),
  ADD KEY `bongkarFK2` (`id_biaya`);

--
-- Indexes for table `cherry`
--
ALTER TABLE `cherry`
  ADD PRIMARY KEY (`id_cherry`),
  ADD KEY `cherryFK1` (`id_panen`);

--
-- Indexes for table `gabah_basah`
--
ALTER TABLE `gabah_basah`
  ADD PRIMARY KEY (`id_gabahB`),
  ADD KEY `gabahBFK1` (`id_cherry`);

--
-- Indexes for table `gabah_kering`
--
ALTER TABLE `gabah_kering`
  ADD PRIMARY KEY (`id_gabahK`),
  ADD KEY `gabahKFK1` (`id_gabahB`);

--
-- Indexes for table `grading`
--
ALTER TABLE `grading`
  ADD PRIMARY KEY (`id_grading`),
  ADD KEY `gradingFK1` (`id_bean`),
  ADD KEY `gradingFK2` (`id_biaya`);

--
-- Indexes for table `green_bean`
--
ALTER TABLE `green_bean`
  ADD PRIMARY KEY (`id_bean`),
  ADD KEY `beanFK1` (`id_gabahK`);

--
-- Indexes for table `hand_pick`
--
ALTER TABLE `hand_pick`
  ADD PRIMARY KEY (`id_hand_pick`),
  ADD KEY `pickFK1` (`id_bean`),
  ADD KEY `pickFK2` (`id_biaya`);

--
-- Indexes for table `hull`
--
ALTER TABLE `hull`
  ADD PRIMARY KEY (`id_hull`),
  ADD KEY `hullFK1` (`id_gabahK`),
  ADD KEY `hullFK2` (`id_biaya`);

--
-- Indexes for table `jemurB`
--
ALTER TABLE `jemurB`
  ADD PRIMARY KEY (`id_jemurB`),
  ADD KEY `jemurBFK1` (`id_gabahB`),
  ADD KEY `jemurBFK2` (`id_biaya`);

--
-- Indexes for table `jemurK`
--
ALTER TABLE `jemurK`
  ADD PRIMARY KEY (`id_jemurK`),
  ADD KEY `jemurKFK1` (`id_gabahK`),
  ADD KEY `jemurKFK2` (`id_biaya`);

--
-- Indexes for table `panen`
--
ALTER TABLE `panen`
  ADD PRIMARY KEY (`id_panen`);

--
-- Indexes for table `sorter`
--
ALTER TABLE `sorter`
  ADD PRIMARY KEY (`id_sorter`),
  ADD KEY `sortFK1` (`id_bean`),
  ADD KEY `sortFK2` (`id_biaya`);

--
-- Indexes for table `suton`
--
ALTER TABLE `suton`
  ADD PRIMARY KEY (`id_suton`),
  ADD KEY `sutonFK1` (`id_bean`),
  ADD KEY `sutonFK2` (`id_biaya`);

--
-- Indexes for table `transport`
--
ALTER TABLE `transport`
  ADD PRIMARY KEY (`id_transport`),
  ADD KEY `transFK1` (`id_gabahB`),
  ADD KEY `transFK2` (`id_biaya`);

--
-- Indexes for table `wetmill`
--
ALTER TABLE `wetmill`
  ADD PRIMARY KEY (`id_wetmill`),
  ADD KEY `wetmillFK1` (`id_cherry`),
  ADD KEY `wetmillFK2` (`id_biaya`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `biaya`
--
ALTER TABLE `biaya`
  MODIFY `id_biaya` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;
--
-- AUTO_INCREMENT for table `bongkar`
--
ALTER TABLE `bongkar`
  MODIFY `id_bongkar` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `cherry`
--
ALTER TABLE `cherry`
  MODIFY `id_cherry` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `gabah_basah`
--
ALTER TABLE `gabah_basah`
  MODIFY `id_gabahB` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `gabah_kering`
--
ALTER TABLE `gabah_kering`
  MODIFY `id_gabahK` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `grading`
--
ALTER TABLE `grading`
  MODIFY `id_grading` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `green_bean`
--
ALTER TABLE `green_bean`
  MODIFY `id_bean` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `hand_pick`
--
ALTER TABLE `hand_pick`
  MODIFY `id_hand_pick` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `hull`
--
ALTER TABLE `hull`
  MODIFY `id_hull` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `jemurB`
--
ALTER TABLE `jemurB`
  MODIFY `id_jemurB` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `jemurK`
--
ALTER TABLE `jemurK`
  MODIFY `id_jemurK` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `panen`
--
ALTER TABLE `panen`
  MODIFY `id_panen` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `sorter`
--
ALTER TABLE `sorter`
  MODIFY `id_sorter` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `suton`
--
ALTER TABLE `suton`
  MODIFY `id_suton` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `transport`
--
ALTER TABLE `transport`
  MODIFY `id_transport` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `wetmill`
--
ALTER TABLE `wetmill`
  MODIFY `id_wetmill` int(10) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `bongkar`
--
ALTER TABLE `bongkar`
  ADD CONSTRAINT `bongkarFK1` FOREIGN KEY (`id_gabahB`) REFERENCES `gabah_basah` (`id_gabahB`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `bongkarFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `cherry`
--
ALTER TABLE `cherry`
  ADD CONSTRAINT `cherryFK1` FOREIGN KEY (`id_panen`) REFERENCES `panen` (`id_panen`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `gabah_basah`
--
ALTER TABLE `gabah_basah`
  ADD CONSTRAINT `gabahBFK1` FOREIGN KEY (`id_cherry`) REFERENCES `cherry` (`id_cherry`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `gabah_kering`
--
ALTER TABLE `gabah_kering`
  ADD CONSTRAINT `gabahKFK1` FOREIGN KEY (`id_gabahB`) REFERENCES `gabah_basah` (`id_gabahB`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `grading`
--
ALTER TABLE `grading`
  ADD CONSTRAINT `gradingFK1` FOREIGN KEY (`id_bean`) REFERENCES `green_bean` (`id_bean`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `gradingFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `green_bean`
--
ALTER TABLE `green_bean`
  ADD CONSTRAINT `beanFK1` FOREIGN KEY (`id_gabahK`) REFERENCES `gabah_kering` (`id_gabahK`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `hand_pick`
--
ALTER TABLE `hand_pick`
  ADD CONSTRAINT `pickFK1` FOREIGN KEY (`id_bean`) REFERENCES `green_bean` (`id_bean`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pickFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `hull`
--
ALTER TABLE `hull`
  ADD CONSTRAINT `hullFK1` FOREIGN KEY (`id_gabahK`) REFERENCES `gabah_kering` (`id_gabahK`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `hullFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `jemurB`
--
ALTER TABLE `jemurB`
  ADD CONSTRAINT `jemurBFK1` FOREIGN KEY (`id_gabahB`) REFERENCES `gabah_basah` (`id_gabahB`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `jemurBFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `jemurK`
--
ALTER TABLE `jemurK`
  ADD CONSTRAINT `jemurKFK1` FOREIGN KEY (`id_gabahK`) REFERENCES `gabah_kering` (`id_gabahK`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `jemurKFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sorter`
--
ALTER TABLE `sorter`
  ADD CONSTRAINT `sortFK1` FOREIGN KEY (`id_bean`) REFERENCES `green_bean` (`id_bean`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sortFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `suton`
--
ALTER TABLE `suton`
  ADD CONSTRAINT `sutonFK1` FOREIGN KEY (`id_bean`) REFERENCES `green_bean` (`id_bean`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sutonFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transport`
--
ALTER TABLE `transport`
  ADD CONSTRAINT `transFK1` FOREIGN KEY (`id_gabahB`) REFERENCES `gabah_basah` (`id_gabahB`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `transFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `wetmill`
--
ALTER TABLE `wetmill`
  ADD CONSTRAINT `wetmillFK1` FOREIGN KEY (`id_cherry`) REFERENCES `cherry` (`id_cherry`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `wetmillFK2` FOREIGN KEY (`id_biaya`) REFERENCES `biaya` (`id_biaya`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
