-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 24 fév. 2023 à 10:57
-- Version du serveur : 8.0.27
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `bddcomptes`
--

-- --------------------------------------------------------

--
-- Structure de la table `adherent`
--

DROP TABLE IF EXISTS `adherent`;
CREATE TABLE IF NOT EXISTS `adherent` (
  `idAdherent` int NOT NULL AUTO_INCREMENT,
  `nomAdherent` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `prenomAdherent` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `codepostalAdherent` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `villeAdherent` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idAdherent`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `adherent`
--

INSERT INTO `adherent` (`idAdherent`, `nomAdherent`, `prenomAdherent`, `codepostalAdherent`, `villeAdherent`) VALUES
(1, 'Ait Alla', 'Yassine', '92700', 'Colombes'),
(2, 'Zaion', 'Sofiane', '92230', 'Gennevilliers'),
(3, 'Jacques', 'Buffeteau', '92230', 'Gennevilliers');

-- --------------------------------------------------------

--
-- Structure de la table `auteurs`
--

DROP TABLE IF EXISTS `auteurs`;
CREATE TABLE IF NOT EXISTS `auteurs` (
  `idAuteur` int NOT NULL AUTO_INCREMENT,
  `nomAuteur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `prenomAuteur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idAuteur`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auteurs`
--

INSERT INTO `auteurs` (`idAuteur`, `nomAuteur`, `prenomAuteur`) VALUES
(1, 'Hugo', 'Victor'),
(2, 'De la fontaine', 'Jean');

-- --------------------------------------------------------

--
-- Structure de la table `collections`
--

DROP TABLE IF EXISTS `collections`;
CREATE TABLE IF NOT EXISTS `collections` (
  `idCollection` int NOT NULL AUTO_INCREMENT,
  `nomCollection` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idCollection`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `collections`
--

INSERT INTO `collections` (`idCollection`, `nomCollection`) VALUES
(1, 'Bibyaso'),
(2, 'Hachette');

-- --------------------------------------------------------

--
-- Structure de la table `emprunter`
--

DROP TABLE IF EXISTS `emprunter`;
CREATE TABLE IF NOT EXISTS `emprunter` (
  `idEmprunt` int NOT NULL AUTO_INCREMENT,
  `idAdherent` int NOT NULL,
  `idLivre` int NOT NULL,
  `dateEmprunt` date NOT NULL,
  `dateRetour` date NOT NULL,
  PRIMARY KEY (`idEmprunt`),
  KEY `num_adherent` (`idAdherent`,`idLivre`),
  KEY `num_livre` (`idLivre`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `emprunter`
--

INSERT INTO `emprunter` (`idEmprunt`, `idAdherent`, `idLivre`, `dateEmprunt`, `dateRetour`) VALUES
(54, 3, 7, '2023-02-23', '2024-02-23');

-- --------------------------------------------------------

--
-- Structure de la table `livre`
--

DROP TABLE IF EXISTS `livre`;
CREATE TABLE IF NOT EXISTS `livre` (
  `idLivre` int NOT NULL AUTO_INCREMENT,
  `titreLivre` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `idAuteur` int NOT NULL,
  `idCollection` int NOT NULL,
  `etatLivre` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idLivre`),
  KEY `id_auteur` (`idAuteur`),
  KEY `livre_ibfk_1` (`idCollection`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `livre`
--

INSERT INTO `livre` (`idLivre`, `titreLivre`, `idAuteur`, `idCollection`, `etatLivre`) VALUES
(1, 'Les misérables', 1, 1, 'Disponible'),
(7, 'le théatre de victor hugo', 1, 2, 'Emprunter');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `idUtilisateur` int NOT NULL AUTO_INCREMENT,
  `nomUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `prenomUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `emailUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `telephoneUtilisateur` varchar(100) NOT NULL,
  `questionutilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `reponseUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `motdepasseUtilisateur` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `confirmemotdepasseUtilisateur` varchar(100) NOT NULL,
  PRIMARY KEY (`idUtilisateur`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`idUtilisateur`, `nomUtilisateur`, `prenomUtilisateur`, `emailUtilisateur`, `telephoneUtilisateur`, `questionutilisateur`, `reponseUtilisateur`, `motdepasseUtilisateur`, `confirmemotdepasseUtilisateur`) VALUES
(1, 'AITALLA', 'Yassine', 'yassine.aitalla@imie-paris.fr', '0650015167', 'Prénom', 'Yassine', 'Yss@2001@?', 'Yss@2001@?'),
(2, 'Zaion', 'Sofiane', 'Sofiane.Zaion@imie-paris.fr', '0620304050', 'Lieu de naissance', 'Gennevilliers', 'Sof@92230@?', 'Sof@92230@?'),
(3, 'Buffeteau', 'Jacques', 'Jacquesbuffeteau@gmail.com', '0620304050', 'Prénom', 'Jacques', 'Jacq@2323', 'Jacq@2323');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `emprunter`
--
ALTER TABLE `emprunter`
  ADD CONSTRAINT `emprunter_ibfk_1` FOREIGN KEY (`idLivre`) REFERENCES `livre` (`idLivre`),
  ADD CONSTRAINT `emprunter_ibfk_2` FOREIGN KEY (`idAdherent`) REFERENCES `adherent` (`idAdherent`);

--
-- Contraintes pour la table `livre`
--
ALTER TABLE `livre`
  ADD CONSTRAINT `livre_ibfk_1` FOREIGN KEY (`idCollection`) REFERENCES `collections` (`idCollection`),
  ADD CONSTRAINT `livre_ibfk_2` FOREIGN KEY (`idAuteur`) REFERENCES `auteurs` (`idAuteur`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
